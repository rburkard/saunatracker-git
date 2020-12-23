from django.contrib import admin
from django.urls import path
from trackerapp import views
from trackerapp.views import ChartView

urlpatterns = [
    path('', ChartView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
]
