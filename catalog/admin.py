from django.contrib import admin
from .models import Location, Image

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']  # Поля для списка объектов
    search_fields = ('title',)  # Поиск по названию
    ordering = ('title',)  # Сортировка по названию


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['location', 'uploaded_at']



