from django.conf import settings
from django.db import models
from django.utils.timezone import now


class LCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Category(models.Model):
    name = LCharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ("name", "owner")


class Expense(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Expenses"
        ordering = ("-created_at",)
