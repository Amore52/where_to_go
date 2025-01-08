
from django.contrib import admin
from .models import Location, Image


class ImageInline(admin.TabularInline):  # Используем TabularInline или StackedInline
    model = Image
    extra = 1
    fields = ['image', 'image_preview',  'position']
    ordering = ['position']
    readonly_fields = ['image_preview']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']  # Поля для списка объектов
    search_fields = ('title',)  # Поиск по названию
    ordering = ('title',)  # Сортировка по названию
    inlines = [ImageInline]





