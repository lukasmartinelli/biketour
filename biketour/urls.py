from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from gps import views as gps_views

urlpatterns = patterns('',
    url(r'^$', gps_views.map, name='home'),
    url(r'^gps/', include('gps.urls')),
    url(r'^twitter/', include('twitter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
