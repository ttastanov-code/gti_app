from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, HomeBlockCreateView, HomeBlockUpdateView

app_name = "main"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blocks/create/", HomeBlockCreateView.as_view(), name="block_create"),
    path("blocks/<int:pk>/edit/", HomeBlockUpdateView.as_view(), name="block_edit"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]
