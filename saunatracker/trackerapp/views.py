from django.shortcuts import render

# Create your views here.

from .models import Track


def index(request):
    output = Track.objects.all()
    return HttpResponse(output)