import os
from django.conf.urls import patterns, url
from django.views.static import serve
from django.conf import settings



urlpatterns = patterns('main.views',
    url(r'^$', 'home_page', name='home-page'),
    url(r'^downloads/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.MEDIA_ROOT, 'downloads'), }),
)
