import re
import csv
import time
import pypac
from contextlib import closing
from bs4 import BeautifulSoup
from pypac import *
import pprint
import webbrowser

music = [
    'Tool',
    'A Perfect Circle',
    'Puscifer',
    'The Black Angels',
    'Nouvelle Vague',
    'Carina round',
    'The Offpsring',
    'Chelsea Wolfe',
    'Radiohead',
    'Camera Obscura',
    'Modest Mouse',
    'Angus & Julia Stone',
    'Bon Iver',
    'Sleeping At Last',
    'Metallica',
    'The Weeknd',
    'Smashing Pumpkins',
    'Sigur Ros',
    'Regina Spektor',
    'Scala & Kolacny Brothers',
    'BrownBoot',
    'Mogwai',
    'Slipknot',
    'Portishead',
    'The Handsome Family',
    'Post Malone',
    'Rammstein',
    'Emily Haines & The Soft Skeleton',
    'Emaily Haines',
    'Metric',
    'Mamiffer',
    'Magic Sword',
    'Elizaveta',
    'Blind Pilot',
    'Barcelona',
    'Inara George',
    'The Bird and The Bee',
    'Ainjel Emme',
    'Garfunkel and Oates',
    'Mazzy Star',
    'Rage Against the Machine',
    'The Black Keys',
    'Florence + The Machine',
    'Angela McCluskey',
    'Sumac',
    'Deftones',
    'Serj Tankian',
    'Kate Micucci',
    'Band of Horses',
    'Nine Inch Nails',
    'Brian Reitzell',
    'Howard Shore',
    'The Killers',
    'The Heavy',
    'The Fray',
    'Georgi Kay',
    'Kittie',
    'Maps to Bears',
    'Elena Siegman',
    'Malukah',
    'BOY',
    'James Blake',
    'Cary Brothers',
    'Childish Gambino',
    'Waz',
    'Aloe Blacc',
    'Ramin Djawadi',
    'Paz Lenchantin'
]

events = []

s = PACSession()
s.headers = {
    'User-Agent': 'python-requests/2.22.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer EG3WOJERNSQLBPG3SJM6'
 }

url = R'https://www.eventbriteapi.com/v3/events/search/?location.address=seattle&location.within=200km'

response = s.get(url)
while response.json()['pagination']['has_more_items']:
    pageNumber = int(response.json()['pagination']['page_number']) + 1
    for x in response.json()['events']:
        if x['name']['text'] in music:
            print('{} is playing!'.format(x['name']['text']))
    response=s.get('https://www.eventbriteapi.com/v3/events/search/?location.address=seattle&location.within=200km&page={}'.format(pageNumber))
    print('Next page!')
else:
    for x in response.json()['events']:
        if x['name']['text'] in music:
            print('{} is playing!'.format(x['name']['text']))