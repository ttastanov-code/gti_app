from django.shortcuts import get_object_or_404
from .models import Page, Vacancy
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import VacancyForm, PageForm

class VacancyListView(ListView):
    model = Vacancy
    template_name = "info/vacancy_list.html"
    context_object_name = "vacancies"

    def get_queryset(self):
        return Vacancy.objects.filter(is_active=True).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Вакансии"
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = "info/vacancy_detail.html"
    context_object_name = "vacancy"

    def get_queryset(self):
        return Vacancy.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = "info/page.html"
    context_object_name = "page"

    def get_object(self):
        page_type = self.kwargs.get("page_type")
        return get_object_or_404(Page, page_type=page_type, is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object

        context["seo_title"] = obj.seo_title or obj.title
        context["seo_description"] = obj.seo_description or obj.title
        context["seo_keywords"] = obj.seo_keywords

        context["page_title"] = obj.title
        return context


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "info/vacancy_create.html"
    success_url = reverse_lazy("info:vacancy_list")


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "info/vacancy_edit.html"

    def get_success_url(self):
        return reverse_lazy("info:vacancy_detail", kwargs={"pk": self.object.pk})
    
    
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "info/page_edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "info:page",
            kwargs={"page_type": self.object.page_type}
        )
