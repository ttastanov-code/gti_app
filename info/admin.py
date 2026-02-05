from django.contrib import admin
from django.utils.html import format_html
from .models import Page, Vacancy, Video

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "page_type", "is_active", "updated_at")
    list_editable = ("is_active",)
    search_fields = ("title",)
    list_filter = ("page_type", "is_active")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("page_type",)

    fieldsets = (
        ("Основное", {
            "fields": ("page_type", "title", "is_active"),
        }),
        ("Контент", {
            "fields": ("content",),
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "description": "Поля для поисковой оптимизации. Если оставить пустыми — будут использованы значения по умолчанию."
        }),
        ("Служебная информация", {
            "fields": ("created_at", "updated_at"),
        }),
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_link", "created_at")
    readonly_fields = ("video_link",)

    def video_link(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                obj.file.url,
                obj.file.url
            )
        return "—"

    video_link.short_description = "URL видео"