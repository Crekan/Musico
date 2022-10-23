from django.views.generic import ListView
from home.models import *
from .models import *


class About(ListView):
    model = AboutArea
    template_name = 'about/about.html'
    context_object_name = 'home_about_area_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_url_video'] = AboutVideo.objects.all()
        context['home_galleries_list'] = GalleriesModel.objects.all()
        return context
