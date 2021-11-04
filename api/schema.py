import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from expenses.models import Expense, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "created_at")


class ExpenseType(DjangoObjectType):
    # categories = graphene.List(
    #     lambda: CategoryType
    # )

    class Meta:
        model = Expense
        fields = (
            "id",
            "name",
            "amount",
            # "categories",
            "created_at",
        )

    # @classmethod
    # def resolve_categories(expense, *args, **kwargs):
    #     return expense.categories.all()


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
