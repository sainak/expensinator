from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .schema import schema
from .views import PrivateGraphQLView

urlpatterns = [
    path(
        "graphql", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema))
    ),
]
