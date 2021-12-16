from django import forms
from django.forms import widgets
from django.utils.timezone import now, timedelta
from django_filters import (
    ChoiceFilter,
    DateRangeFilter,
    FilterSet,
    ModelChoiceFilter,
    OrderingFilter,
)

from expenses.models import Expense
from categories.models import Category


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


class StatisticsFilterForm(forms.Form):
    error_css_class = "is-invalid"
    user = None

    start_date = forms.DateField(
        widget=widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Start date",
        required=False,
        initial=lambda: now().date() - timedelta(days=30),
    )
    end_date = forms.DateField(
        widget=widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="End date",
        required=False,
        initial=lambda: now().date(),
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=widgets.SelectMultiple(attrs={"class": "form-select"}),
        required=False,
    )

    scale_type = forms.ChoiceField(
        choices=(
            ("day", "Day"),
            ("week", "Week"),
            ("month", "Month"),
            ("quarter", "Quarter"),
            ("year", "Year"),
        ),
        widget=widgets.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        categories_field = self.fields["categories"]
        categories_field.queryset = Category.objects.filter(owner=self.user)
        categories_field.widget.attrs["class"] = "form-select"
        categories_field.empty_label = "Uncategorized"
        categories_field.required = False
