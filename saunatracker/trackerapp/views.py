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


def index(request):
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


    ## Create today df

    user_selection_day = 0
    current_week = datetime.date.today().isocalendar()[1]

    current_day_df = df[(df['weeknr'] == current_week) & (df['weekday'] == user_selection_day)]

    plot_current_day_df = current_day_df[['current_count', 'hour']]

    plot_current_day_df = plot_current_day_df.groupby('hour').mean()


    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(plot_current_day_df.index, plot_current_day_df.current_count)

    html1 = mpld3.fig_to_html(fig)
    return HttpResponse(html1)
    """


    ## Create past average df

    four_week_back = datetime.date.today() + relativedelta(months=-1)
    four_week_back = four_week_back.isocalendar()[1]

    average_df = df[(df['weeknr'] >= four_week_back) & (df['weekday'] == user_selection_day)]
    plot_average_df = average_df[['current_count', 'hour']]

    plot_average_df = plot_average_df.groupby('hour').mean()

    html = (plot_current_day_df.to_html(),plot_average_df.to_html()) 
    return HttpResponse(html)