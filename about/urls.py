from django.urls import path
from .views import *

urlpatterns = [
    path('about/', About.as_view(), name='about'),
]
