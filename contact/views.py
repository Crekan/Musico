from django.shortcuts import render
from .models import *


def contact(request):
    contact = Locate.objects.all()

    context = {
        'contact': contact,
    }
    return render(request, 'contact/contact.html', context)
