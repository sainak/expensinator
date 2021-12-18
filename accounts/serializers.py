from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id", "last_login")
