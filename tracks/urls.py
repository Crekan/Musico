from django.urls import path
from .views import *

urlpatterns = [
    path('tracks/', Tracks.as_view(), name='tracks'),
]
