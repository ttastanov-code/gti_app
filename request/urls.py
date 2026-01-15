from django.urls import path
from .views import RequestCreateView

app_name = "request"

urlpatterns = [
    path("", RequestCreateView.as_view(), name="form"),
]
