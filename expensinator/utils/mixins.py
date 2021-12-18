from rest_framework.permissions import AllowAny


class PublicApiViewMixin:
    """
    Allow public access to the endpoint.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)


class ModelOwnerMixin:
    """
    Restrict access to the endpoint to the owner of the model.
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
