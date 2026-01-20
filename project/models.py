from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Project(models.Model):
    name = models.CharField("Название проекта", max_length=200)
    image = models.ImageField("Иллюстрация", upload_to="projects/")
    description = HTMLField("Описание проекта")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    # SEO
    seo_title = models.CharField(
        "SEO Title",
        max_length=255,
        blank=True
    )
    seo_description = models.TextField(
        "SEO Description",
        blank=True
    )
    seo_keywords = models.CharField(
        "SEO Keywords",
        max_length=500,
        blank=True
    )
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("project:detail", kwargs={"pk": self.pk})