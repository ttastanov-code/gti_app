from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    image = models.ImageField("Иллюстрация", upload_to="articles/")
    content = HTMLField("Текст новости или статьи")
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    # SEO
    seo_title = models.CharField(
        "SEO Title",
        max_length=255,
        blank=True,
        help_text="Если пусто — используется обычный заголовок"
    )
    seo_description = models.TextField(
        "SEO Description",
        blank=True,
        help_text="Краткое описание для поисковиков"
    )
    seo_keywords = models.CharField(
        "SEO Keywords",
        max_length=500,
        blank=True,
        help_text="Ключевые слова через запятую"
    )
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"pk": self.pk})
