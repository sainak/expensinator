from django import forms
from django.utils.translation import gettext_lazy as _

from categories.models import Category


class AddCategoryForm(forms.ModelForm):
    error_css_class = "is-invalid"

    class Meta:
        model = Category
        fields = (
            "name",
            "color",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(
                attrs={"class": "form-control form-control-color", "type": "color"}
            ),
        }
