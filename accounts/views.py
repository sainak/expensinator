from django.contrib.auth import get_user_model
from django.contrib.auth import views as contrib_views
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from expensinator.utils.mixins import PublicApiViewMixin

from .forms import LoginForm, SignUpForm
from .serializers import UserSerializer

User = get_user_model()


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


class UserSignUpApiView(PublicApiViewMixin, CreateAPIView):
    serializer_class = UserSerializer


class UserProfileApiView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
