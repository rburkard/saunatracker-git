from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Track


def index(request):
    output = Track.objects.all()
    return HttpResponse(output)