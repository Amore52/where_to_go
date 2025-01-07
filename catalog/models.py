from django.db import models

class Location(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=16, decimal_places=14)
    lat = models.DecimalField(max_digits=16, decimal_places=14)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    location = models.ForeignKey('Location', related_name='images', on_delete=models.CASCADE)  # related_name меняем на 'images'
    image = models.ImageField(upload_to='images/')  # Поле для изображения
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.location.title}"  # Возвращаем название локации в строковом представлении изображения
