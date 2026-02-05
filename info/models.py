from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

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
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("info:page", kwargs={"page_type": self.page_type})


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


class Video(models.Model):
    title = models.CharField("Название", max_length=255)
    file = models.FileField("Видео", upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def url(self):
        if self.file:
            return self.file.url
        return ""