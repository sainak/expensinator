from django.urls import path

from .views import auth, main, expenses

urlpatterns = [
    path("", main.HomeView.as_view(), name="home"),
    path("signup/", auth.SignUpView.as_view(), name="signup"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("expenses/", expenses.ExpenseListView.as_view(), name="expense-list"),
]
