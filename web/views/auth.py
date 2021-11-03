from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import LoginForm, SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "auth/signup.html"


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "auth/login.html"
    next_page = reverse_lazy("home")
