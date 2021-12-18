from rest_framework.routers import DefaultRouter

from ..views import ExpenseApiViewset


router = DefaultRouter(trailing_slash=False)
router.register(r"expenses", ExpenseApiViewset, basename="expenses")

urlpatterns = router.urls
