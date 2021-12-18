from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/verify", TokenVerifyView.as_view(), name="token_verify"),
]
