import os

import pandas as pd
from django.apps import AppConfig

from config.settings.base import ROOT_DIR


class ApiConfig(AppConfig):
    name = 'api'
    dataplant = pd.read_excel(os.path.join(ROOT_DIR, "data/egrid.xlsx"), sheet_name="PLNT19",
                         header=1).fillna('')

    datastate = data = pd.read_excel(os.path.join(ROOT_DIR, "data/egrid.xlsx"), sheet_name="ST19",
                             header=1)
