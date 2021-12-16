import graphene
from graphene_django import DjangoObjectType

from expenses.models import Expense
from categories.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "color",
            "created_at",
        )


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
        fields = (
            "id",
            "name",
            "amount",
            "category",
            "created_at",
        )


class Query(graphene.ObjectType):
    expenses = graphene.List(ExpenseType)
    categories = graphene.List(CategoryType)

    def resolve_expenses(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return Expense.objects.none()
        return Expense.objects.filter(owner=user)

    def resolve_categories(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return Category.objects.none()
        return Category.objects.filter(owner=user)


schema = graphene.Schema(query=Query)
