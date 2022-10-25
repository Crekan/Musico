from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class Home(ListView):
    model = ImageModel
    template_name = 'home/index.html'
    context_object_name = 'images_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries_list'] = GalleriesModel.objects.all()
        context['audio_list'] = AudioArea.objects.all()
        context['latest_tracks_list'] = LatestTracks.objects.all()
        context['about_are_list'] = AboutArea.objects.all()
        return context


def pageNotFound(request, exception):
    return render(request, 'home/404.html')
