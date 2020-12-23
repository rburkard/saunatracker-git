from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.views.generic import TemplateView

# Custom imports

from .models import Track
from .prep_tables import get_today_dataset, get_average_dataset


class ChartView(TemplateView):
    template_name = 'trackerapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today_data = get_today_dataset
        context["qs"] = today_data
        return context
    
    
"""
def index(request):
    (labels, data) = get_today_dataset()
    return JsonResponse(data = {
        'labels': labels,
        'data' : data
    })
"""