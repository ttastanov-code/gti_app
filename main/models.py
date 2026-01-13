from django.db import models
from tinymce.models import HTMLField

class HomeBlock(models.Model):
    title = models.CharField("Заголовок блока", max_length=200)
    content = HTMLField("Содержимое блока")
    order = models.PositiveIntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Home Block"
        verbose_name_plural = "Home Blocks"
        ordering = ["order"]

    def __str__(self):
        return self.title
