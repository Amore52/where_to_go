from django.db import models
from django.utils.html import mark_safe
from tinymce.models import HTMLField

class Location(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    location = models.ForeignKey('Location', related_name='image', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
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
