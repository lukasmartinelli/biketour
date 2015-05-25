from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biketour.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gps/', include('gps.urls')),
    url(r'^twitter/', include('twitter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
