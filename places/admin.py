from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Location, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ["image", "image_preview", "position"]
    ordering = ["position"]
    readonly_fields = ["image_preview"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded_at"]
    search_fields = ("title",)
    ordering = ("title",)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "location", "uploaded_at", "position"]
    search_fields = ("location__title",)
    ordering = ("location", "position")
    raw_id_fields = ["location"]
    readonly_fields = ["image_preview"]
