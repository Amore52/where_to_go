from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from .models import Location, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ['image', 'image_preview',  'position']
    ordering = ['position']
    readonly_fields = ['image_preview']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [ImageInline]





