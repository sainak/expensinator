from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class ExpenseListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    redirect_field_name = "next"
    template_name = "expenses/expense_list.html"
