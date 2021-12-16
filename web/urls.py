from django.urls import path
from django.urls.conf import include

from .views import main

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("", include("accounts.urls.web")),
    path("", include("expenses.urls.web")),
    path("", include("categories.urls.web")),
    path("", include("stats.urls.web")),
]
