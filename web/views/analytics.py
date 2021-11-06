from datetime import datetime, timedelta
from typing import List, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet, Sum, DateField
from django.db.models.functions import Extract, Trunc
from django.utils.timezone import get_current_timezone
from django.views.generic import TemplateView

from expenses.models import Category, Expense


def get_graph_data(
    categories: List[Category],
    qs: QuerySet[Expense],
    end_date: datetime,
    start_date: Optional[datetime] = None,
    group_type: Optional[str] = "day",
):
    # quick sanity check
    if group_type not in ["day", "week", "quarter", "month", "year"]:
        return {}

    if not start_date:
        start_date = end_date - timedelta(days=30)

    data = {
        "groupType": group_type,
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
                    group_type,
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
                "label": category.name,
                "borderColor": category.color,
                "total": _qs.aggregate(Sum("amount"))["amount__sum"],
                "data": chart_data,
            }
        )
    return data


class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "analytics/analytics_list.html"
    context_object_name = "categories"
    page_name = "Analytics"
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

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        expenses = self.get_queryset()
        cat_chart_data = list(
            expenses.values("category")
            .annotate(amount_sum=Sum("amount"))
            .values_list("category__name", "category__color", "amount_sum")
        )
        context["categoriesChartData"] = list(zip(*cat_chart_data))
        categories = Category.objects.filter(owner=self.request.user)

        context["lineChartData"] = get_graph_data(
            categories, self.get_queryset(), end_date=datetime.now(), group_type="day"
        )

        return self.render_to_response(context)
