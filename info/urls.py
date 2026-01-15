from django.urls import path
from .views import (
    VacancyListView,
    VacancyDetailView,
    VacancyCreateView,
    VacancyUpdateView,
    PageDetailView,
    PageUpdateView,
)

app_name = "info"

urlpatterns = [
    # Вакансии
    path("vacancies/", VacancyListView.as_view(), name="vacancy_list"),
    path("vacancies/create/", VacancyCreateView.as_view(), name="vacancy_create"),
    path("vacancies/<int:pk>/", VacancyDetailView.as_view(), name="vacancy_detail"),
    path("vacancies/<int:pk>/edit/", VacancyUpdateView.as_view(), name="vacancy_edit"),

    # Универсальные страницы
    path("page/<str:page_type>/", PageDetailView.as_view(), name="page"),
    path("page/<int:pk>/edit/", PageUpdateView.as_view(), name="page_edit"),

]
