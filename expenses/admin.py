from django.contrib import admin

from .models import Category, Expense


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "created_at")
