from typing import List
from datetime import date, datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions.datetime import Now
from django.db.models.query import QuerySet
from django.http import request
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear

from expenses.models import Category, Expense


def get_graph(
    categories: List[Category],
    qs: QuerySet[Expense],
    end_date: date,
    start_date: date = None,
    group_type: str = "date",
):
    data = {}

    if not start_date:
        start_date = end_date - timedelta(days=30)

    # quick sanity check
    if group_type not in ["date", "month", "year"]:
        return

    group_type = f"created_at__{group_type}"
    for category in categories:
        cat = {
            "color": category.color,
            "total": 0.0,
        }
        cqs = qs.filter(category=category).filter(
            created_at__gte=start_date, created_at__lte=end_date
        )
        cat["total"] = cqs.aggregate(Sum("amount"))["amount__sum"]
        graph_data = (
            cqs.values(group_type)
            .annotate(amount_sum=Sum("amount"))
            .values_list(group_type, "amount_sum")
        )
        cat["graph"] = list(zip(*graph_data))
        data[category.name] = cat

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

        context["lineChartData"] = get_graph(
            categories, self.get_queryset(), end_date=datetime.now(), group_type="year"
        )

        return self.render_to_response(context)
