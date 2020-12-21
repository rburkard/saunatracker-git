import requests
import urllib.request
import time
import datetime
from bs4 import BeautifulSoup


from dateutil.parser import parse 
from dateutil.relativedelta import relativedelta
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd



# Import Data and clean
df = pd.read_csv('sample_data.csv', parse_dates=['date'])

df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.time

print(df['time'])
df = df[(df['time'] >= pd.to_datetime('09:00:00')) & (df['time'] <= pd.to_datetime('19:00:00'))]

## Create correct dataframe, goal:
# count # date # # time # weekday # hour # weeknumber

df['weekday'] = [d.weekday() for d in df.date]
df['hour'] = [d.hour for d in df.time]
df['weeknr'] = [d.isocalendar()[1] for d in df.date]


## Create today df

user_selection_day = 1
current_week = datetime.date.today().isocalendar()[1]

current_day_df = df[(df['weeknr'] == current_week) & (df['weekday'] == user_selection_day)]

plt.plot(current_day_df.hour, current_day_df.current_count)


## Create past average df

four_week_back = datetime.date.today() + relativedelta(months=-1)
four_week_back = four_week_back.isocalendar()[1]

average_df = df[(df['weeknr'] >= four_week_back) & (df['weekday'] == user_selection_day)]
average_df = average_df[['current_count', 'hour']]
average_df = average_df.groupby('hour').mean()

plt.plot(average_df.index, average_df.current_count)
plt.show()