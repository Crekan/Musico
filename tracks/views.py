from django.shortcuts import render
from .models import *
from home.models import *


def tracks(request):
    tracks_area = TracksMusicArea.objects.all()
    home_images_list = ImageModel.objects.all()

    context = {
        'tracks_area': tracks_area,
        'home_images_list': home_images_list,
    }
    return render(request, 'tracks/track.html', context)
