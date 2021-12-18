from django.urls import path

from ..views import CategoryListApiView

urlpatterns = [
    path("", view=CategoryListApiView.as_view(), name="api-categories-list"),
]
