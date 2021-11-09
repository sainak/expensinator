from datetime import datetime, timedelta
from typing import List, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import DateField, QuerySet, Sum
from django.db.models.functions import Extract, Trunc
from django.http.response import JsonResponse
from django.utils.timezone import get_current_timezone, now
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormMixin

from expenses.models import Category, Expense

from ..filters import StatisticsFilterForm


def get_graph_data(
    categories: List[Category],
    qs: QuerySet[Expense],
    end_date: datetime,
    start_date: Optional[datetime] = None,
    scale_type: Optional[str] = "day",
):
    # quick sanity check
    if scale_type not in ["day", "week", "month", "quarter", "year"]:
        return {}

    if not start_date:
        start_date = end_date - timedelta(days=30)

    data = {
        "scaleType": scale_type,
        "categories": [],
    }
    for category in categories:
        _qs = qs.filter(category=category).filter(
            created_at__gte=start_date,
            created_at__lte=end_date,
        )
        chart_data = list(
            _qs.annotate(
                date=Trunc(
                    "created_at",
                    scale_type,
                    output_field=DateField(),
                    tzinfo=get_current_timezone(),
                ),
            )
            .values("date")
            .annotate(
                x=Extract("date", "epoch"),
                y=Sum("amount"),
            )
            .values("x", "y")
            .order_by("x")
        )
        data["categories"].append(
            {
                "label": category.name if category else "Uncategorized",
                "borderColor": category.color if category else "#000000",
                #"total": _qs.aggregate(Sum("amount"))["amount__sum"],
                "data": chart_data,
            }
        )
    return data


class StatisticsView(LoginRequiredMixin, FormMixin, TemplateView):

    form_class = StatisticsFilterForm
    template_name = "statistics/statistics_list.html"
    context_object_name = "categories"
    page_name = "Statistics"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
        "opacity": "95",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).select_related(
            "category"
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        expenses = self.get_queryset()
        cat_chart_data = list(
            expenses.values("category")
            .annotate(amount_sum=Sum("amount"))
            .values_list("category__name", "category__color", "amount_sum")
        )
        context["categoriesChartData"] = list(zip(*cat_chart_data))

        return self.render_to_response(context)


class StatisticsDataView(LoginRequiredMixin, View):
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).select_related(
            "category"
        )

    def get(self, *args, **kwargs):
        end_date = self.request.GET.get("end_date", now())
        start_date = self.request.GET.get("start_date", None)
        scale_type = self.request.GET.get("scale_type", "day")
        _categories = self.request.GET.getlist("categories[]")

        categories = []
        categories_qs = Category.objects.filter(owner=self.request.user)
        if _categories:
            try:
                _categories.remove("")
                categories.append(None)
            except ValueError:
                pass
            categories_qs = categories_qs.filter(id__in=_categories)
        else:
            categories.append(None)
        categories.extend(list(categories_qs))

        return JsonResponse(
            get_graph_data(
                categories,
                self.get_queryset(),
                end_date,
                start_date=start_date,
                scale_type=scale_type,
            )
        )
