import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    csv_file = settings.BUS_STATION_CSV
    with open(csv_file, newline='') as f:
        bus_stations = list(csv.DictReader(f))
        paginator = Paginator(bus_stations, 10)
        page_obj = paginator.get_page(page_number)
        context = {
            'bus_stations': page_obj.object_list,
            'page': page_obj,
        }
    return render(request, 'stations/index.html', context)
