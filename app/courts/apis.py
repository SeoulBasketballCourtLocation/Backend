import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings.base import ROOT_DIR
from courts.models import Court
from courts.serializers import CourtSerializer


class CourtList(APIView):
    def get(self, request, format=None):
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
        serializer = CourtSerializer(courts, many=True)
        return Response(serializer.data)