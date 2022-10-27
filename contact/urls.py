from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact')
]
