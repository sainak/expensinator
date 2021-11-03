from django.contrib.auth import views as contrib_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import LoginForm, SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "auth/signup.html"
    extra_context = {
        "title": "SignUp | Expensinator",
        "activeNavId": "navItemSignUp",
    }


class LoginView(contrib_views.LoginView):
    form_class = LoginForm
    template_name = "auth/login.html"
    next_page = reverse_lazy("home")
    extra_context = {
        "title": "Login | Expensinator",
        "activeNavId": "navItemLogin",
    }


class LogoutView(contrib_views.LogoutView):
    template_name = None
    next_page = reverse_lazy("login")
