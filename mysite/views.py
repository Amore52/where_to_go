from django.shortcuts import render
from django.http import JsonResponse
from catalog.models import Location, Image
import json

def main_page(request):
    places_data = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "/static/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "/static/places/roofs24.json"
            }
        }
    ]

    # Преобразуем данные в JSON строку
    places_geojson = json.dumps(places_data)

    return render(request, 'index.html', {
        'places_geojson': places_geojson,
    })
