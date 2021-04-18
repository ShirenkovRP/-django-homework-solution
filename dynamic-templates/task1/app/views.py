import csv
from django.shortcuts import render
from django.conf import settings


def inflation_view(request):
    template_name = 'inflation.html'

    tab = []
    with open(settings.INFLATION_RUSSIA_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            row_list = []
            for g in i:
                if "." in g:
                    row_list.append(float(g))
                else:
                    row_list.append((g))
            tab.append(row_list)

    context = {"tab": tab}

    return render(request, template_name,
                  context)
