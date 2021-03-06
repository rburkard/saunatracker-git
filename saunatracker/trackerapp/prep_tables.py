from django.shortcuts import render
from django.http import HttpResponse

# Custom imports

from .models import Track
import pandas as pd
import datetime

from dateutil.parser import parse 
from dateutil.relativedelta import relativedelta
import matplotlib as mpl
import seaborn as sns
import numpy as np

## graph by mpld3
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

df = pd.DataFrame(list(Track.objects.all().values()))

df = df.rename(columns={"count": "current_count"})

df['date_time'] = pd.to_datetime(df['date_time'])
df['time'] = df['date_time'].dt.strftime('%H:%M')

## Create correct dataframe, goal:
# count # date # # time # weekday # hour # weeknumber

df['weekday'] = [d.weekday() for d in df.date_time]
df['hour'] = [d.hour for d in df.date_time]
df['weeknr'] = [d.isocalendar()[1] for d in df.date_time]

# Only show opening times
df = df[(df['hour'] >= 9)&(df['hour'] < 19)] 


def get_average_dataset():
    ## Create today df

    four_week_back = datetime.date.today() + relativedelta(months=-1)
    four_week_back = four_week_back.isocalendar()[1]

    average_df = df[(df['weeknr'] >= four_week_back)]

    average_df = average_df[['current_count', 'weekday', 'hour']]

    res = []

    ## Not clean: fix the data creation another time (filling up with zeroes)
    for day in range(7):
        temp_df = average_df[(average_df['weekday'] == day)]
        temp_df = temp_df.groupby('hour').mean()
        temp_df['current_count'] = temp_df['current_count'].round(1)
        data = temp_df.iloc[:, 0].tolist()
        if len(data) != 11:
            fix_data = []
            for i in range(11):
                try:
                    fix_data.append(data[i])
                except IndexError:
                    fix_data.extend([0])
            res.append(fix_data)
            continue
        res.append(data)
    return res
