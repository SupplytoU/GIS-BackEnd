import requests
from django.contrib.gis.geos import Point

def calculate_distance(origin: Point, destination: Point) -> float:
    # Coordinates in longitude,latitude format
    coordinates = f"{origin.x},{origin.y};{destination.x},{destination.y}"

    url = f"http://router.project-osrm.org/route/v1/driving/{coordinates}?overview=false"

    response = requests.get(url)
    data = response.json()

    distance = data['routes'][0]['distance'] / 1000.0

    return distance