from main.mixins import BaseListView, BaseDetailView
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ArticleForm
from .models import Article


class ArticleListView(BaseListView):
    model = Article
    template_name = "article/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by("-published_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Статьи и новости"
        context["page_description"] = "Актуальные новости и статьи компании"
        return context


class ArticleDetailView(BaseDetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/article_edit.html"

    def get_success_url(self):
        return reverse_lazy("article:detail", kwargs={"pk": self.object.pk})
    
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/article_edit.html"

    def get_success_url(self):
        return reverse_lazy("article:detail", kwargs={"pk": self.object.pk})
    
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/article_create.html"

    def get_success_url(self):
        return reverse_lazy("article:detail", kwargs={"pk": self.object.pk})