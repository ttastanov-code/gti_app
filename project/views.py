from .models import Project
from main.mixins import BaseListView, BaseDetailView
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProjectForm

class ProjectListView(BaseListView):
    model = Project
    template_name = "project/project_list.html"
    context_object_name = "projects"
    ordering = "-created_at"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Наши проекты"
        return context


class ProjectDetailView(BaseDetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.name
        return context


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_edit.html"

    def get_success_url(self):
        return reverse_lazy("project:detail", kwargs={"pk": self.object.pk})
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_create.html"

    def get_success_url(self):
        return reverse_lazy("project:detail", kwargs={"pk": self.object.pk})