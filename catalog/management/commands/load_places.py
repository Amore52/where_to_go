import json
import os
from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from catalog.models import Location, Image


class Command(BaseCommand):
    help = "Load places from JSON files in a directory"

    def add_arguments(self, parser):
        parser.add_argument('directory_path', type=str, help="Path to the directory containing JSON files")

    def handle(self, *args, **kwargs):
        directory_path = kwargs['directory_path']

        for file_name in os.listdir(directory_path):
            if file_name.endswith('.json'):
                file_path = os.path.join(directory_path, file_name)
                self.stdout.write(self.style.NOTICE(f"Loading data from {file_path}"))

                with open(file_path, 'r', encoding='utf-8') as file:
                    location_json = json.load(file)

                place, created = Location.objects.get_or_create(
                    title=location_json['title'],
                    defaults={
                        'description_short': location_json['description_short'],
                        'description_long': location_json['description_long'],
                        'lng': location_json['coordinates']['lng'],
                        'lat': location_json['coordinates']['lat'],
                    }
                )

                for img_url in location_json['imgs']:
                    response = requests.get(img_url)
                    if response.status_code == 200:
                        image_name = os.path.basename(urlparse(img_url).path)
                        image_instance = Image(location=place)
                        image_instance.image.save(image_name, ContentFile(response.content), save=True)

                self.stdout.write(self.style.SUCCESS(f"Place '{place.title}' loaded successfully."))

