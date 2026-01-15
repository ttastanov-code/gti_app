from django.db import models
from tinymce.models import HTMLField

class Page(models.Model):
    PAGE_TYPES = [
        ('about', 'О нас'),
        ('cooperation', 'Сотрудничество'),
        ('faq', 'F.A.Q.'),
    ]
    page_type = models.CharField("Тип страницы", max_length=20, choices=PAGE_TYPES)
    title = models.CharField("Заголовок", max_length=200)
    content = HTMLField("Содержимое")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField("Должность", max_length=200)
    description = HTMLField("Описание вакансии")
    requirements = HTMLField("Требования", blank=True)
    responsibilities = HTMLField("Обязанности", blank=True)
    is_active = models.BooleanField("Вакансия активна", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.title
