from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("updated_at",)
    ordering = ("-created_at",)

    fieldsets = (
        ("Основное", {
            "fields": ("name", "image", "description")
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "description": "Поля для поисковой оптимизации. Можно оставить пустыми."
        }),
        ("Служебная информация", {
            "fields": ("created_at", "updated_at"),
        }),
    )
