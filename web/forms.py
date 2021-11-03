from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class LoginForm(AuthenticationForm):

    required_css_class = "required"

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)

    class Meta:
        model = User
        fields = ("username", "password")
