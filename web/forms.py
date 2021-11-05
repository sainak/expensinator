from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import fields
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from expenses.models import Category, Expense

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class LoginForm(AuthenticationForm):

    error_messages = {
        "invalid_login": _("Invalid credentials. "),
        "inactive": _("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ("username", "password")


class AddExpenseForm(forms.ModelForm):

    error_css_class = "is-invalid"
    user = None
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(owner=user),
        widget=forms.widgets.Select(attrs={"class": "form-select"}),
        required=False,
    )

    created_at = forms.CharField(
        widget=widgets.TextInput(attrs={"type": "hidden"}),
        initial=now,
    )

    class Meta:
        model = Expense
        fields = (
            "name",
            "amount",
            "category",
            "created_at",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)


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
