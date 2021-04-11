import csv
import urllib.parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    # Отображение списока остановок наземного общественного транспорта.
    list_of_stops = []
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stopping_dict = {"Name": row["Name"], "Street": row["Street"], "District": row["District"]}
            list_of_stops.append(stopping_dict)

    # Создание страниц и постраничного отображения
    paginator = Paginator(list_of_stops, 9)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    if page.has_previous():
        prev_page_url = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': page.previous_page_number()})
    else:
        prev_page_url = None
    if page.has_next():
        next_page_url = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': page.next_page_number()})
    else:
        next_page_url = None

    context = {
        'bus_stations': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render(request, 'index.html', context=context)
