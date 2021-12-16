from django.urls import path
from django.urls.conf import include

from .views import main, statistics

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("", include("accounts.urls.web")),
    path("", include("expenses.urls.web")),
    path("", include("categories.urls.web")),
    path("statistics/", statistics.StatisticsView.as_view(), name="statistics-list"),
    path(
        "statistics/data",
        statistics.StatisticsDataView.as_view(),
        name="statistics-data",
    ),
]
