from django.urls import path

from .views import auth, expenses, main

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("signup/", auth.SignUpView.as_view(), name="signup"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("expenses/", expenses.ExpenseListView.as_view(), name="expenses-list"),
]
