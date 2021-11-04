from django_filters import FilterSet, ModelMultipleChoiceFilter, OrderingFilter, DateFromToRangeFilter, DateRangeFilter

from expenses.models import Category, Expense


def categories(request):
    if request is None:
        return Category.objects.none()
    return Category.objects.filter(owner=request.user)


class ExpenseFilter(FilterSet):
    categories = ModelMultipleChoiceFilter(queryset=categories, label="Category")
    o = OrderingFilter(
        fields=(("created_at", "time"),),
        field_labels={
            "created_at": "Created at",
        },
    )
    created_at = DateRangeFilter()

    class Meta:
        model = Expense
        fields = ("categories", "created_at")
