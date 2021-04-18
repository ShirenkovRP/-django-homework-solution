import csv
from django.shortcuts import render
from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'

    with open(settings.INFLATION_RUSSIA_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        tab = list(reader)

    context = {"tab": tab}

    return render(request, template_name,
                  context)
