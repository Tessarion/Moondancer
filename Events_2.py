import re
import csv
import time
import pypac
from contextlib import closing
from bs4 import BeautifulSoup
from pypac import *
import pprint
import webbrowser


events = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Events.txt'
ht = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Events.html'
ft = R'C:\Users\ky275e\Documents\Projects\Python\New_Scraper\Events\Free_Events.html'

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

city = 'seattle'
searchRange = '10km'

def apiBoy():
    url = R'https://www.eventbriteapi.com/v3/events/search/?location.address={}&location.within={}&start_date.keyword=this_weekend'.format(city, searchRange)
    page = s.get(url)
    while page.json()['pagination']['has_more_items']:
        pageNumber = int(page.json()['pagination']['page_number']) + 1
        for x in page.json()['events']:
            if x['subcategory_id'] in coolCodes:
                cool_Events.append(x)
        page = s.get(R'https://www.eventbriteapi.com/v3/events/search/?location.address=seattle&location.within=10km&start_date.keyword=this_weekend&page={}'.format(str(pageNumber)))
    else:
        for x in page.json()['events']:
            if x['subcategory_id'] in coolCodes:
                cool_Events.append(x)

apiBoy()



def allEvents():
    with open(ht, mode='r+') as pageboy:
        pageboy.write('<!DOCTYPE html> \n <html> \n <body> \n <h1>Events this weekend</h1>')
        for x in cool_Events:
            pageboy.write('<a href="{}">{}</a><br>'.format(x['url'], x['name']['text']))
            pageboy.write('<p>{}</p>'.format(x['start']['local'][:9]))
            pageboy.write('<p>{}</p>'.format(x['description']['text']))