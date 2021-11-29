import json

from django.db import models
from django.db.models import Sum


# Create your models here.
class PLNT(models.Model):
    SEQPLT19 = models.IntegerField()
    PSTATABB = models.CharField(max_length=10)
    PNAME = models.CharField(max_length=100)
    LAT = models.CharField(max_length=20)
    LON = models.CharField(max_length=20)
    PLNGENAN = models.FloatField()


class State(models.Model):
    PSTATABB = models.CharField(max_length=100)
    STNGENAN = models.FloatField()
    geometry = models.JSONField()

    @property
    def calculate_percentage(self):
        total = State.objects.aggregate(Sum('STNGENAN'))['STNGENAN__sum']

        try:
            return round((self.STNGENAN / total) * 100, 2)
        except ZeroDivisionError:
            return 0
