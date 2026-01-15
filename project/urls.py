from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView

app_name = "project"

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("create/", ProjectCreateView.as_view(), name="create"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", ProjectUpdateView.as_view(), name="edit"),
]
