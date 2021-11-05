from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"
    page_name = "Home"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("expenses-list"))
        return super().get(request, *args, **kwargs)
