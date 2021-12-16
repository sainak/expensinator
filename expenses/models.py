from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Expense(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        "categories.Category", null=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Expenses"
        ordering = ("-created_at",)
