#!/usr/bin/env python3.8
# -*- coding: ascii -*-

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saunatracker.settings')

application = get_wsgi_application()

from trackerapp.models import Track

import requests
import urllib.request
import time
import datetime
from bs4 import BeautifulSoup

# creating object 
current_time = datetime.datetime.today().timetuple()

# displaying the tuples of the object
if current_time.tm_hour >= 8 and current_time.tm_hour < 20:
    for i in range(4):
        url = 'https://www.seebadenge.ch/wp/sauna'
        response = requests.get(url)
        print(response)
        print(current_time.tm_hour)

        soup = BeautifulSoup(response.text, "html.parser")
        c_count = soup.findAll('span')[-3].text

        print(c_count)
        Track(count = c_count).save()
        time.sleep(900)