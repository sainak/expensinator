from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from rest_framework.generics import ListCreateAPIView

from categories.models import Category
from categories.serializers import CategorySerializer

from .forms import AddCategoryForm


class CategoriesListView(LoginRequiredMixin, ListView):

    template_name = "categories_list.html"
    paginate_by = 20
    context_object_name = "categories_list"
    page_name = "Categories"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "opacity": "95",
    }

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoriesCreateView(LoginRequiredMixin, CreateView):

    template_name = "categories_form.html"
    model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy("categories-list")
    page_name = "New Category"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemCategories",
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            form.add_error("name", "Category already exists")
            form["name"].field.widget.attrs["class"] += " is-invalid"
            return self.form_invalid(form)


class CategoriesEditView(LoginRequiredMixin, UpdateView):

    template_name = "categories_form.html"
    model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy("categories-list")
    page_name = "Edit Category"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemCategories",
    }

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            form.add_error("name", "Category already exists")
            form["name"].field.widget.attrs["class"] += " is-invalid"
            return self.form_invalid(form)


class CategoriesDeleteView(LoginRequiredMixin, View):
    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        category = get_object_or_404(self.get_queryset(), pk=id)
        category.delete()
        return HttpResponseRedirect(reverse_lazy("categories-list"))


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
