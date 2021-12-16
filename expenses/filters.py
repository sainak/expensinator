from django import forms
from django_filters import DateRangeFilter, FilterSet, ModelChoiceFilter, OrderingFilter

from categories.models import Category

from .models import Expense


def get_categories(request):
    if request is None:
        return Category.objects.none()
    return Category.objects.filter(owner=request.user)


class ExpenseFilter(FilterSet):
    category = ModelChoiceFilter(
        queryset=get_categories,
        label="Category",
        widget=forms.Select(attrs={"class": "form-select"}),
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
        fields = ("category", "created_at")
