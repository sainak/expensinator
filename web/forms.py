from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import fields
from django.utils.translation import gettext_lazy as _

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

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={"class": "form-select"}),
        required=False,
    )

    class Meta:
        model = Expense
        fields = (
            "name",
            "amount",
            "categories",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["categories"].queryset = Category.objects.filter(owner=self.user)


class AddCategoryForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = Category
        fields = ("name",)
