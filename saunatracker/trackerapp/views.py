from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Import models
from .models import Track

# Import data
from .prep_tables import get_average_dataset


class ChartView(TemplateView):
    template_name = 'trackerapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        average_data = get_average_dataset
        context["qs"] = average_data
        return context