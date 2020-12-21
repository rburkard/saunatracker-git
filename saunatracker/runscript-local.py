import requests
import urllib.request
import time
import datetime
from bs4 import BeautifulSoup

for i in range(60):

    # creating object 
    current_time = datetime.datetime.today().timetuple()
    
    # displaying the tuples of the object
    if current_time.tm_hour >= 8 and current_time.tm_hour < 20:
        print(current_time) 
    
    else:
        time.sleep(60)

    url = 'https://www.seebadenge.ch/wp/sauna'
    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    c_count = soup.findAll('span')[-3].text

    print(c_count)
    Track(count = c_count).save()
    time.sleep(600)