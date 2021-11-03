from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, SignUpForm


class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy("home")
