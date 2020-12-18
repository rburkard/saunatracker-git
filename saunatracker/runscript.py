from trackerapp.models import Track

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

while True:
    url = 'https://www.seebadenge.ch/wp/sauna'
    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    counter = soup.findAll('span')[-3]
    counter = str(counter)
    
    c_count = ""
    for i in counter:
        if i.isnumeric():
            c_count += i

    c_time = time.time()

    Track(count = c_count).save()
    time.sleep(1800)