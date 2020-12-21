from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Track
import pandas as pd
import datetime


def index(request):
    df = pd.DataFrame(list(Track.objects.all().values()))
    html = df.to_html()
    return HttpResponse(html)