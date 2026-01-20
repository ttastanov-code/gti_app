from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "published_at", "updated_at")
    list_editable = ("is_published",)
    search_fields = ("title",)
    list_filter = ("is_published", "published_at")
    readonly_fields = ("published_at", "updated_at")
    ordering = ("-published_at",)

    fieldsets = (
        ("Основное", {
            "fields": ("title", "image", "is_published"),
        }),
        ("Контент", {
            "fields": ("content",),
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "description": "SEO-настройки для поисковых систем. Можно оставить пустыми."
        }),
        ("Служебная информация", {
            "fields": ("published_at", "updated_at"),
        }),
    )
