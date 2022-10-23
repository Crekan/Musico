from django.urls import path
from .views import *

urlpatterns = [
    path('tracks/', tracks, name='tracks'),
]
