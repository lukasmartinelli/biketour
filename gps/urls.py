from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^log$', views.log, name='log'),
    url(r'^track$', views.track, name='track'),
    url(r'^track/current$', views.current_position, name='current_position'),
    url(r'^map$', views.map, name='map'),
    url(r'^upload$', views.upload_gpx, name='upload'),
]
