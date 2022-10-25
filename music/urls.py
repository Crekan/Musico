from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('tracks.urls')),
    path('', include('blog.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    re_path(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

