from django import forms
from django_filters import (
    DateRangeFilter,
    FilterSet,
    ModelMultipleChoiceFilter,
    OrderingFilter,
)

from expenses.models import Category, Expense


def categories(request):
    if request is None:
        return Category.objects.none()
    return Category.objects.filter(owner=request.user)


class ExpenseFilter(FilterSet):
    categories = ModelMultipleChoiceFilter(
        queryset=categories,
        label="Category",
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        distinct=True,
    )
    o = OrderingFilter(
        fields=(("created_at", "time"),),
        field_labels={
            "created_at": "Created at",
        },
        # custom widget is broken in this filter
    )
    created_at = DateRangeFilter(
        widget=forms.Select(attrs={"class": "form-select"}), empty_label="All"
    )

    class Meta:
        model = Expense
        fields = ("categories", "created_at")
