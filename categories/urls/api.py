from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views import CategoryApiViewset


router = DefaultRouter(trailing_slash=False)
router.register(r"categories", CategoryApiViewset, basename="categories")

urlpatterns = router.urls
