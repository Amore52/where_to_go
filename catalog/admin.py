from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Поля для списка объектов
    search_fields = ('title',)  # Поиск по названию
    ordering = ('title',)  # Сортировка по названию

admin.site.register(Location, LocationAdmin)

