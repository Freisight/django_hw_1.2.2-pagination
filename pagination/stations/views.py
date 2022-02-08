from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
import csv


with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    new_data = []
    for row in reader:
        item = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
        new_data.append(item)
        # new_data = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}

CONTENT = [str(i) for i in range(100)]
def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'stations/pagi.html', context=context)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(new_data, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page
    }


    return render(request, 'stations/index.html', context=context)
