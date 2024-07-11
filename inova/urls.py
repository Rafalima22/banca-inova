from django.urls import path
from inova.views import home


urlpatterns = [
    path('', home),
]