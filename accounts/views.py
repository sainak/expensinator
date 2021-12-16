from django.contrib.auth import views as contrib_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    page_name = "SignUp"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }


class LoginView(contrib_views.LoginView):
    form_class = LoginForm
    template_name = "login.html"
    next_page = reverse_lazy("home")
    page_name = "Login"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }


class LogoutView(contrib_views.LogoutView):
    template_name = None
    next_page = reverse_lazy("login")
