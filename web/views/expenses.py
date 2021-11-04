from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django_filters.views import FilterView

from expenses.models import Category, Expense

from ..filters import ExpenseFilter


class ExpenseListView(LoginRequiredMixin, FilterView):

    filterset_class = ExpenseFilter

    login_url = reverse_lazy("login")
    template_name = "expenses/expense_list.html"
    paginate_by = 20
    context_object_name = "expenses_list"
    page_name = "Expenses"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class CategoriesListView(LoginRequiredMixin, ListView):

    login_url = reverse_lazy("login")
    template_name = "expenses/categories_list.html"
    paginate_by = 20
    context_object_name = "categories_list"
    page_name = "Categories"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
