from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Track
import pandas as pd
import datetime

from dateutil.parser import parse 
from dateutil.relativedelta import relativedelta
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def index(request):
    df = pd.DataFrame(list(Track.objects.all().values()))


    df['date_time'] = pd.to_datetime(df['date_time'])
    df['time'] = df['date_time'].dt.time


    ## Create correct dataframe, goal:
    # count # date # # time # weekday # hour # weeknumber

    df['weekday'] = [d.weekday() for d in df.date_time]
    df['weeknr'] = [d.isocalendar()[1] for d in df.date_time]
    df['hour'] = [d.hour for d in df.time]

    opening_time = datetime.datetime.strptime('09:00:00', '%H:%M:%S')

    closing_time = datetime.datetime.strptime('19:00:00', '%H:%M:%S')

    html = df.to_html()
    return HttpResponse(html)


    df = df[(df['time'] >= opening_time) & (df['time'] <= closing_time)]


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