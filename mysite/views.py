from django.shortcuts import render
from django.http import JsonResponse
from catalog.models import Location, Image
import json

def main_page(request):
    places_data = []
    locations = Location.objects.all()

    for location in locations:
        images = Image.objects.filter(location=location)
        image_urls = [image.image.url for image in images]
        place_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]  # Долгота и широта
            },
            "properties": {
                "title": location.title,
                "placeId": location.id,
                "detailsUrl": f"/places/{location.id}/",
                "imgs": image_urls
            }
        }
        places_data.append(place_info)
    places_geojson = json.dumps(places_data)
    return render(request, 'index.html', {
        'places_geojson': places_geojson,
    })


def place_details(request, place_id):
    try:
        location = Location.objects.get(id=place_id)
        images = Image.objects.filter(location=location)
        return JsonResponse({
            'title': location.title,
            'description_short': location.description_short,
            'description_long': location.description_long,
            'imgs': [image.image.url for image in images],
        })
    except Location.DoesNotExist:
        return JsonResponse({'error': 'Place not found'}, status=404)
