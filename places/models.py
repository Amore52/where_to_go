from django.db import models
from django.utils.html import mark_safe
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = HTMLField(verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(
        'Location', related_name='image', on_delete=models.CASCADE, blank=True, null=True
    )
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиция")

    class Meta:
        ordering = ['position']

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: auto;" />')
        return "Нет изображения"

    image_preview.short_description = "Превью"

    def __str__(self):
        return f"Image for {self.location.title}"
