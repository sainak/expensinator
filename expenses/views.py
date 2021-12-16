from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View
from django_filters.views import FilterView

from .models import Expense
from .filters import ExpenseFilter
from .forms import AddExpenseForm


class ExpenseListView(LoginRequiredMixin, FilterView):

    filterset_class = ExpenseFilter
    template_name = "expense_list.html"
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

    template_name = "expense_form.html"
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


class ExpenseEditView(LoginRequiredMixin, UpdateView):
    template_name = "expense_form.html"
    form_class = AddExpenseForm
    success_url = reverse_lazy("expenses-list")
    page_name = "Edit Expense"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemExpenses",
        "currency": "₹",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).select_related(
            "category"
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, View):
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).select_related(
            "category"
        )

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        expense = get_object_or_404(self.get_queryset(), pk=id)
        expense.delete()
        return HttpResponseRedirect(reverse_lazy("expenses-list"))
