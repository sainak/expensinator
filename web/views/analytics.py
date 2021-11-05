from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from expenses.models import Category, Expense


class AnalyticsView(LoginRequiredMixin, ListView):
    template_name = "analytics/analytics_list.html"
    context_object_name = "categories"
    page_name = "Analytics"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
    }

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expense.objects.all()
        return context
