from django import forms
from django.forms import widgets
from django.utils.timezone import now, timedelta

from categories.models import Category


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
