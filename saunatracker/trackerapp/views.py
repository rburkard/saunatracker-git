from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Track


def index(request):
    output = Track.objects.all()
    res = []
    for i in output:
        observation = []
        observation.append(i.count)
        observation.append(i.date_time)
        res.append(observation)

    # format
    finalstr = ""
    for i in res:
        finalstr += f"{i} \n"
    return HttpResponse(finalstr)