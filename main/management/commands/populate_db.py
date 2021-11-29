import json
import os

import pandas as pd
from django.core.management.base import BaseCommand

from config.settings.base import ROOT_DIR
from main.models import PLNT, State
import json


class Command(BaseCommand):
    help = 'Import data from eGrid XLSX file to postgres DB'

    def handle(self, *args, **options):
        # PLANTS DATA
        data = pd.read_excel(os.path.join(ROOT_DIR, "data/egrid.xlsx"), sheet_name="PLNT19", usecols='A,C:E,T,U,AN',
                             header=1)
        data = data.dropna(subset=['PLNGENAN'])
        for index, row in data.iterrows():
            PLNT.objects.get_or_create(SEQPLT19=row['SEQPLT19'], PSTATABB=row['PSTATABB'], PNAME=row['PNAME'],
                                       LAT=row['LAT'], LON=row['LON'], PLNGENAN=row['PLNGENAN'])

        # STATES DATA
        data = pd.read_excel(os.path.join(ROOT_DIR, "data/egrid.xlsx"), sheet_name="ST19", usecols='B,I',
                             header=1)
        with open(os.path.join(ROOT_DIR, 'data/map-data.json'), 'r', encoding='utf-8') as cats:
            map_data = json.load(cats)

        for index, row in data.iterrows():
            State.objects.get_or_create(PSTATABB=row['PSTATABB'], STNGENAN=row['STNGENAN'],geometry=map_data[row['PSTATABB']])
