from django.db.models import Avg
from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster

from TboProject.models import ObjectLocations


def index(request):
    avg_lat = ObjectLocations.objects.aggregate(avg=Avg('latitude'))['avg']

    stations = ObjectLocations.objects.all()
    # stations = EVChargingLocation.objects.exclude(latitude__gt=avg_lat)
    m = folium.Map(location=[51.6666, 39.2016], zoom_start=2)
        # for stat in stations:
        #     coordinates = (stat.longitude, station.latitude)
        #     folium.Marker(coordinates, popup=stat.station_name).add_to(m)

    latitueds = [station.longitude for station in stations]
    longituedes = [station.latitude for station in stations]

    FastMarkerCluster(data=list(zip(latitueds, longituedes))).add_to(m)
    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)

