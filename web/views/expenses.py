from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django_filters.views import FilterView

from expenses.models import Category, Expense

from ..filters import ExpenseFilter
from ..forms import AddCategoryForm, AddExpenseForm


class ExpenseListView(LoginRequiredMixin, FilterView):

    filterset_class = ExpenseFilter
    template_name = "expenses/expense_list.html"
    paginate_by = 20
    context_object_name = "expenses_list"
    page_name = "Expenses"
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


class ExpenseCreateView(LoginRequiredMixin, CreateView):

    template_name = "expenses/expense_create.html"
    form_class = AddExpenseForm
    success_url = reverse_lazy("expenses-list")
    page_name = "Add Expense"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemExpenses",
        "currency": "₹",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CategoriesListView(LoginRequiredMixin, ListView):

    template_name = "expenses/categories_list.html"
    paginate_by = 20
    context_object_name = "categories_list"
    page_name = "Categories"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "opacity": "95",
    }

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoriesCreateView(LoginRequiredMixin, CreateView):

    template_name = "expenses/categories_create.html"
    model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy("categories-list")
    page_name = "New Category"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemCategories",
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            form.add_error("name", "Category already exists")
            form["name"].field.widget.attrs["class"] += " is-invalid"
            return self.form_invalid(form)
