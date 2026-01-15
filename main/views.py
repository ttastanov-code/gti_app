from django.views.generic import TemplateView
from .models import HomeBlock
from article.models import Article
from project.models import Project


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blocks"] = HomeBlock.objects.filter(is_active=True)
        context["articles"] = Article.objects.order_by("-published_at").filter(is_published=True)[:3]
        context["projects"] = Project.objects.order_by("-created_at").all()[:6]
        context["page_title"] = "Главная"
        return context
