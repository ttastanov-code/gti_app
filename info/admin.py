from django.contrib import admin
from .models import Page, Vacancy

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_type', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('page_type', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('page_type',)
    fieldsets = (
        ("Основное", {
            "fields": ("page_type", "title", "is_active")
        }),
        ("Контент", {
            "fields": ("content",),
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
