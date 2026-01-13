# project/models.py
from django.db import models
from tinymce.models import HTMLField

class Project(models.Model):
    name = models.CharField("Название проекта", max_length=200)
    image = models.ImageField("Иллюстрация", upload_to="projects/")
    description = HTMLField("Описание проекта")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
