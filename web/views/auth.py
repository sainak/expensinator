from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import LoginForm, SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"
    next_page = reverse_lazy("home")
    redirect_field_name='next'

    # def get_redirect_url(self):
    #     """Return the user-originating redirect URL if it's safe."""
    #     redirect_to = self.request.GET.get(self.redirect_field_name, '')
    #     return redirect_to
