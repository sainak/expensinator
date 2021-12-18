from rest_framework.permissions import AllowAny


class PublicApiViewMixin:
    """
    Allow public access to the endpoint.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
