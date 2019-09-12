import csv
import time
import pypac
from contextlib import closing
from bs4 import BeautifulSoup
from pypac import *
import pprint
import webbrowser
from datetime import datetime

locationURL= R'http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={}&q={}'
primeURL = R'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}?apikey={}'

s = PACSession()
apiKey = R'BmWazvnmhmuKFAxrcGYG7kR1kOFBfHMF'
locationDict = {
    '98031' : ['Kent'],
    '98361' : ['Paradise'],
    '98022' : ['Greenwater', '41278_PC'],
    '98068' : ['Snoqualmie'],
    '98362' : ['Olympic National Park']
}

for k, v in locationDict.items():
    r = s.get(locationURL.format(apiKey, k))
    locationDict[k].append(r.json()[0]['Key'])
    print(r.json()[0]['Key'])
    r = s.get(primeURL.append(locationDict[k][1], apiKey))
    print(locationDict[k][0])
    print(r.json()['Headline']['Text'])
    for x in r.json()['DailyForecasts']:
        print(time.strftime('%B %d, %Y', time.localtime(x['EpochDate'])))
        print('High of {} | Low of {} {}'.format(x['Temperature']['Maximum']['Value'], x['Temperature']['Minimum']['Value']))
        print('Day conditions: {} | Night conditions: {}'.format(x['Day']['IconPhrase'], x['Night']['IconPhrase']))
        
