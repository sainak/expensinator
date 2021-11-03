from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView

from expenses.models import Expense


class ExpenseListView(LoginRequiredMixin, ListView):

    login_url = reverse_lazy("login")
    template_name = "expenses/expense_list.html"
    paginate_by = 15
    context_object_name = "expenses_list"
    page_name = "Expenses"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
