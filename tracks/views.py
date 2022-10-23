from django.views.generic import ListView

from .models import *
from home.models import *


class Tracks(ListView):
    model = TracksMusicArea
    template_name = 'tracks/track.html'
    context_object_name = 'tracks_area'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_images_list'] = ImageModel.objects.all()
        return context
