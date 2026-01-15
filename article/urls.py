from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleCreateView

app_name = "article"

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="edit"),
]
