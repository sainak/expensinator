from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django_filters.views import FilterView, FilterMixin
from django.db.models import Sum

from expenses.models import Category, Expense


class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "analytics/analytics_list.html"
    context_object_name = "categories"
    page_name = "Analytics"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).select_related(
            "category"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, *args, **kwargs):
        expenses = self.get_queryset()
        g = list(
            expenses.values("category")
            .annotate(amount_sum=Sum("amount"))
            .values_list("category__name", "category__color", "amount_sum")
        )
        print(g)
        context = self.get_context_data(**kwargs)
        context["g"] = g
        return self.render_to_response(context)
