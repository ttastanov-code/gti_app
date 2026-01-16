# request/models.py
from django.db import models
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField


class Request(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    phone = PhoneNumberField("Телефон", region=None)
    message = HTMLField("Сообщение")
    file = models.FileField(
        "Файл (ТЗ, документы)",
        upload_to="requests/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_processed = models.BooleanField("Обработано", default=False)

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"
        ordering = ['-created_at']