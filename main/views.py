from django.views.generic import TemplateView, CreateView, UpdateView
from .models import HomeBlock
from article.models import Article
from project.models import Project
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HomeBlock
from .forms import HomeBlockForm
from django.http import HttpResponse
from django.views import View


class RobotsTxtView(View):
    def get(self, request):
        content = (
            "User-agent: *\n"
            "Allow: /\n\n"
            "Sitemap: https://guidejet.kz/sitemap.xml"
        )
        return HttpResponse(content, content_type="text/plain")
    
    
class HomeBlockCreateView(LoginRequiredMixin, CreateView):
    model = HomeBlock
    form_class = HomeBlockForm
    template_name = "main/homeblock_create.html"

    def get_success_url(self):
        return reverse_lazy("main:home")


class HomeBlockUpdateView(LoginRequiredMixin, UpdateView):
    model = HomeBlock
    form_class = HomeBlockForm
    template_name = "main/homeblock_edit.html"

    def get_success_url(self):
        return reverse_lazy("main:home")
    

class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blocks"] = HomeBlock.objects.filter(is_active=True)
        context["articles"] = Article.objects.order_by("-published_at").filter(is_published=True)[:4]
        context["projects"] = Project.objects.order_by("-created_at").all()[:8]
        context["page_title"] = "Главная"
        return context
