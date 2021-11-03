from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"
    page_name = "Home"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }
