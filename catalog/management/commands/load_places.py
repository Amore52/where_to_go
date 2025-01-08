import json
import os
from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from catalog.models import Location, Image


class Command(BaseCommand):
    help = "Load places from JSON file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the JSON file with place data")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Create or get location
        place, created = Location.objects.get_or_create(
            title=data['title'],
            defaults={
                'description_short': data['description_short'],
                'description_long': data['description_long'],
                'lng': data['coordinates']['lng'],
                'lat': data['coordinates']['lat'],
            }
        )

        # Add images
        for img_url in data['imgs']:
            response = requests.get(img_url)
            if response.status_code == 200:
                image_name = os.path.basename(urlparse(img_url).path)
                image_instance = Image(location=place)
                image_instance.image.save(image_name, ContentFile(response.content), save=True)

        self.stdout.write(self.style.SUCCESS(f"Place '{place.title}' loaded successfully."))
