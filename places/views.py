import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Location, Image


def main_page(request):
    locations_geojson = []
    locations = Location.objects.all()

    for location in locations:
        details_url = reverse("place_details", kwargs={"place_id": location.id})
        place_properties = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat],
            },
            "properties": {
                "title": location.title,
                "placeId": location.id,
                "detailsUrl": details_url,
            },
        }
        locations_geojson.append(place_properties)
    places_geojson = json.dumps(locations_geojson, ensure_ascii=False, indent=2)

    return render(request, "index.html", {
        "places_geojson": places_geojson,
    })


def place_details(request, place_id):
    location = get_object_or_404(Location.objects.prefetch_related('image'), id=place_id)
    images = location.image.all()
    return JsonResponse({
        "title": location.title,
        "description_short": location.short_description,
        "description_long": location.long_description,
        "imgs": [image.image.url for image in images],
    })
