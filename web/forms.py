from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class LoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _(
            "Invalid credentials. "
        ),
        'inactive': _("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ("username", "password")
