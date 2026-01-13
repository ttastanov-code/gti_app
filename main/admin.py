from django.contrib import admin
from .models import HomeBlock

@admin.register(HomeBlock)
class HomeBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('order',)
    