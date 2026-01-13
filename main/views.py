from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project.models import Project
from article.models import Article
from main.models import HomeBlock

def index(request):
    projects = Project.objects.all().order_by('-created_at')[:5]
    articles = Article.objects.filter(is_published=True).order_by('-published_at')[:5]
    blocks = HomeBlock.objects.filter(is_active=True).order_by('order')
    return render(request, 'main/index.html', {'projects': projects, 'articles': articles, 'blocks': blocks})
