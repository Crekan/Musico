from django.shortcuts import render
from home.models import *
from .models import *


def about(request):
    home_about_area_list = AboutArea.objects.all()
    about_url_video = AboutVideo.objects.all()
    home_galleries_list = GalleriesModel.objects.all()

    contex = {
        'home_about_area_list': home_about_area_list,
        'about_url_video': about_url_video,
        'home_galleries_list': home_galleries_list,
    }
    return render(request, 'about/about.html', contex)
