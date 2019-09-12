import csv
import time
import pypac
from contextlib import closing
from bs4 import BeautifulSoup
from pypac import *
import pprint
import webbrowser
from datetime import datetime

from header import header
from footer import footer


events = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Events.txt'
ht = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Events.html'
ft = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Free_Events.html'


timeFormatOriginal = '%Y-%m-%d'
eraseMe = R'\r\n\xa0'


coolCodes = [
    '2001',
    '2002',
    '2003',
    '2004',
    '2005',
    '2006',
    '2007',
    '2999',
    '3001',
    '3003',
    '3011',
    '3017',
    '4001',
    '4002',
    '4004',
    '19002',
    '12008',
    '10001',
    '10002',
    '10004',
    '9006',
    '9999',
    '9001',
    '5010'
    ]

cool_Events = []

s = PACSession()

s.headers = {
    'User-Agent': 'python-requests/2.22.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer EG3WOJERNSQLBPG3SJM6'
 }

#city = input("What city would you like to look for events for?")
#searchRange = input("What distance are you willing to travel for an event?")
city = 'Bellevue'
searchRange = '10'
priceyBoy = True

def apiBoy():
    url = R'https://www.eventbriteapi.com/v3/events/search/?location.address={}&location.within={}km&start_date.keyword=this_weekend'.format(city, searchRange)
    page = s.get(url)
    while page.json()['pagination']['has_more_items']:
        pageNumber = int(page.json()['pagination']['page_number']) + 1
        for x in page.json()['events']:
            if x['subcategory_id'] in coolCodes:
                cool_Events.append(x)
        page = s.get(R'https://www.eventbriteapi.com/v3/events/search/?location.address={}&location.within={}km&start_date.keyword=this_weekend&page={}'.format(city, searchRange, str(pageNumber)))
    else:
        for x in page.json()['events']:
            if x['subcategory_id'] in coolCodes:
                cool_Events.append(x)

apiBoy()


def eventPicker():
    if priceyBoy == True:
        expensiveBoy()
    else:
        freeBoy()


def expensiveBoy():
    with open(ht, mode='r+') as pageboy:
        pageboy.write(header)
        for x in cool_Events:
            pageboy.write('<a href="{}">{}</a><br>'.format(x['url'], x['name']['text']))
            rawTime = datetime.strptime(x['start']['local'][:-9], timeFormatOriginal)
            pageboy.write('<p>{}</p>'.format(rawTime.strftime('%A, %B %d, %Y')))
            rawDescription = x['description']['text']
            betterDescription = rawDescription.replace('\r\n', '<br>')
            evenBetterDescription = betterDescription.replace(u'\xa0', u' ')
            theVeryBestDescription = evenBetterDescription.replace(u'\u2013', ' - ')
            slightlyBetterDescription = theVeryBestDescription.replace(u'\u2019', "'")
            comeOnGuys = slightlyBetterDescription.replace(u'\u201C', '"')
            seriouslyThough = comeOnGuys.replace(u'\u201D', '"')
            killMe = seriouslyThough.replace(u'\u2026', '...')
            done = killMe.replace(u'\uFFFD', '')
            #pageboy.write('<p>{}</p>'.format(x['description']['text']))
            pageboy.write('<p>{}</p>'.format(done))
        pageboy.write(footer)
    webbrowser.open_new(ht)

def freeBoy():
    with open(ft, mode='r+') as pageboy:
        pageboy.write('<!DOCTYPE html> \n <html> \n <body> \n <center> \n <h1>Free events this weekend</h1>')
        for x in cool_Events:
            if x['is_free']:
                pageboy.write('<a href="{}">{}</a><br>'.format(x['url'], x['name']['text']))
                rawTime = datetime.strptime(x['start']['local'][:-9], timeFormatOriginal)
                pageboy.write('<p>{}</p>'.format(rawTime.strftime('%A, %B %d, %Y')))
                pageboy.write('<p>{}</p>'.format(x['description']['html']))
                pageboy.write('<br>')
    webbrowser.open_new(ft)

#eventPicker()


expensiveBoy()