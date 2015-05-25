from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^timeline$', views.timeline, name='timeline'),
]
