from rest_framework.routers import SimpleRouter

from ..views import ExpenseApiViewset


router = SimpleRouter(trailing_slash=False)
router.register(r"expenses", ExpenseApiViewset, basename="api-expenses")

urlpatterns = router.urls
