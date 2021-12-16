from django.urls import path

from ..views import (
    CategoriesCreateView,
    CategoriesDeleteView,
    CategoriesEditView,
    CategoriesListView,
)

urlpatterns = [
    path("categories/", CategoriesListView.as_view(), name="categories-list"),
    path(
        "categories/new/",
        CategoriesCreateView.as_view(),
        name="categories-create",
    ),
    path(
        "category/<int:pk>/",
        CategoriesEditView.as_view(),
        name="category-edit",
    ),
    path(
        "category/delete/",
        CategoriesDeleteView.as_view(),
        name="category-delete",
    ),
]
