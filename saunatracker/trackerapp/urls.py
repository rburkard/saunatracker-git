from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('trackerapp/', include('trackerapp.urls')),
    path('admin/', admin.site.urls),
]