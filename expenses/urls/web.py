from django.urls import path

from ..views import (
    ExpenseCreateView,
    ExpenseDeleteView,
    ExpenseEditView,
    ExpenseListView,
)


urlpatterns = [
    path("expenses/", ExpenseListView.as_view(), name="expenses-list"),
    path("expenses/new/", ExpenseCreateView.as_view(), name="expenses-create"),
    path("expense/<int:pk>/", ExpenseEditView.as_view(), name="expense-edit"),
    path(
        "expense/delete/",
        ExpenseDeleteView.as_view(),
        name="expense-delete",
    ),
]
