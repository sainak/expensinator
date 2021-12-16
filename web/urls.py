from django.urls import path
from django.urls.conf import include

from .views import expenses, main, statistics

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("", include("accounts.urls.web")),
    path("", include("expenses.urls.web")),
    path("categories/", expenses.CategoriesListView.as_view(), name="categories-list"),
    path(
        "categories/new/",
        expenses.CategoriesCreateView.as_view(),
        name="categories-create",
    ),
    path(
        "categories/<int:pk>/",
        expenses.CategoriesEditView.as_view(),
        name="category-edit",
    ),
    path(
        "category/delete/",
        expenses.CategoriesDeleteView.as_view(),
        name="category-delete",
    ),
    path("statistics/", statistics.StatisticsView.as_view(), name="statistics-list"),
    path(
        "statistics/data",
        statistics.StatisticsDataView.as_view(),
        name="statistics-data",
    ),
]
