from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from ..views import UserProfileApiView, UserSignUpApiView


urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="api-login"),
    path("login/refresh", TokenRefreshView.as_view(), name="api-token-refresh"),
    path("login/verify", TokenVerifyView.as_view(), name="api-token-verify"),
    path("signup", UserSignUpApiView.as_view(), name="api-signup"),
    path("user", UserProfileApiView.as_view(), name="api-user"),
]
