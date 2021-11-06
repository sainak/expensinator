from django.urls import path

from .views import auth, expenses, main, statistics

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("signup/", auth.SignUpView.as_view(), name="signup"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("expenses/", expenses.ExpenseListView.as_view(), name="expenses-list"),
    path("expenses/new/", expenses.ExpenseCreateView.as_view(), name="expenses-create"),
    path("expenses/<int:pk>/", expenses.ExpenseEditView.as_view(), name="expense-edit"),
    path("categories/", expenses.CategoriesListView.as_view(), name="categories-list"),
    path(
        "categories/new/",
        expenses.CategoriesCreateView.as_view(),
        name="categories-create",
    ),
    path(
        "categories/<int:pk>/",
        expenses.CategoriesEditView.as_view(),
        name="category-edit",
    ),
    path("statistics/", statistics.StatisticsView.as_view(), name="statistics-list"),
    path(
        "statistics/data",
        statistics.StatisticsDataView.as_view(),
        name="statistics-data",
    ),
]
