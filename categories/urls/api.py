from django.urls import path
from rest_framework.routers import SimpleRouter

from ..views import CategoryApiViewset

router = SimpleRouter(trailing_slash=False)
router.register(r"categories", CategoryApiViewset, basename="api-categories")

urlpatterns = router.urls
