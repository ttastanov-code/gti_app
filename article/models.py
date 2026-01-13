from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    image = models.ImageField("Иллюстрация", upload_to="articles/")
    content = HTMLField("Текст новости или статьи")
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
