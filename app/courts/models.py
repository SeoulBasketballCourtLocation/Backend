import json
import os

from django.db import models

from config.settings.base import ROOT_DIR


class Court(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    lat = models.CharField(max_length=255, blank=True)
    lng = models.CharField(max_length=255, blank=True)
    no_basket = models.IntegerField(blank=True)
    bench = models.BooleanField(default=False, blank=True)
    showerbox = models.BooleanField(default=False, blank=True)
    parking = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name



