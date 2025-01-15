import json
import os
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Location, Image


class Command(BaseCommand):
    help = "Load place from a JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="URL to the JSON file with place data")

    def handle(self, *args, **kwargs):
        url = kwargs["url"]
        self.stdout.write(self.style.NOTICE(f"Loading data from {url}"))

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f"Failed to fetch data: {e}"))
            return

        try:
            raw_location = response.json()
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f"Invalid JSON data: {e}"))
            return

        place, created = Location.objects.get_or_create(
            title=raw_location["title"],
            defaults={
                "short_description": raw_location.get("description_short", ""),
                "long_description": raw_location.get("description_long", ""),
                "lng": raw_location["coordinates"]["lng"],
                "lat": raw_location["coordinates"]["lat"],
            }
        )

        for img_url in raw_location.get("imgs", []):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                self.stderr.write(self.style.ERROR(f"Failed to download image {img_url}: {e}"))
                continue

            image_name = os.path.basename(urlparse(img_url).path)
            image_file = ContentFile(img_response.content, name=image_name)
            Image.objects.create(location=place, image=image_file)

        self.stdout.write(self.style.SUCCESS(f"Place '{place.title}' loaded successfully."))
