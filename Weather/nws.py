import csv
import time
import pypac
from contextlib import closing
from bs4 import BeautifulSoup
from pypac import *
import pprint
import webbrowser
from datetime import datetime

s = PACSession()

nws = R'https://api.weather.gov/icons'

weekend = ['Friday', 'Friday Night', 'Saturday', 'Saturday Night', 'Sunday', 'Sunday Night']

burntMountainStationID = 'BUSW1'

dictOfZones = {
    'Greenwater/Mount Rainier' : 'WAZ569',
    'San Juan Islands' : 'WAZ001',
    'Palouse' : 'WAZ033',
    'Spokane' : 'WAZ036',
    'The Gorge' : 'WAZ024',
    'Granite Falls' : 'WAZ568'
}

for k, v in dictOfZones.items():
    url = R'https://api.weather.gov/zones/land/{}/forecast'.format(v)
    response = s.get(url)
    for x in response.json()['periods']:
        if x['name'] in weekend:
            print(k, x['name'])
            print(x['detailedForecast'])