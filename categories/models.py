from django.conf import settings
from django.db import models


class LCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Category(models.Model):
    name = LCharField(max_length=50)
    color = models.CharField(max_length=7, default="#000000")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ("name", "owner")
