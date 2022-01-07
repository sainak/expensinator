from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import UserProfileApiView, UserSignUpApiView
from categories.views import CategoryApiViewset
from expenses.views import ExpenseApiViewset

accounts_urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="api-login"),
    path("login/refresh", TokenRefreshView.as_view(), name="api-token-refresh"),
    path("login/verify", TokenVerifyView.as_view(), name="api-token-verify"),
    path("signup", UserSignUpApiView.as_view(), name="api-signup"),
    path("user", UserProfileApiView.as_view(), name="api-user"),
]


router = DefaultRouter(trailing_slash=False)

router.register(r"categories", CategoryApiViewset, basename="api-categories")
router.register(r"expenses", ExpenseApiViewset, basename="api-expenses")


urlpatterns = router.urls



urlpatterns += [
    path("accounts/", include(accounts_urlpatterns)),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
