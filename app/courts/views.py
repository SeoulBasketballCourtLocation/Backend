import json
import os

from django.shortcuts import render

from config.settings.base import ROOT_DIR
from courts.models import Court


def courts_list(request):
    DATA_DIR = os.path.join(ROOT_DIR, '.data')
    hanriver_courts = json.load(open(os.path.join(DATA_DIR, 'hanriver.json')))
    for court in hanriver_courts['DATA']:
        name = court['bename']
        lat = court['lat']
        lng = court['lng']
        if Court.objects.filter(name__contains=name):
            break
        Court.objects.create(name=name, lat=lat, lng=lng, no_basket=0)
    courts = Court.objects.all()
    context = {
        'courts':courts,
    }
    return render(request, 'courts/courts_list.html', context)

def court_detail(reqeust, pk):
    court = Court.objects.get(pk=pk)
    context = {
        "court":court,
    }
    return render(reqeust, 'courts/court_detail.html', context)