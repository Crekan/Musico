from django.shortcuts import render
from .models import *


def home(request):
    images_list = ImageModel.objects.all()
    galleries_list = GalleriesModel.objects.all()
    audio_list = AudioArea.objects.all()
    latest_tracks_list = LatestTracks.objects.all()
    about_are_list = AboutArea.objects.all()

    context = {
        'images_list': images_list,
        'galleries_list': galleries_list,
        'audio_list': audio_list,
        'latest_tracks_list': latest_tracks_list,
        'about_are_list': about_are_list,
    }
    return render(request, 'home/index.html', context)
