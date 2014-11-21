# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^$','personalsite.views.home'),
    url(r'^about','personalsite.views.about'),
    url(r'^work','personalsite.views.work'),
    url(r'^events','personalsite.views.events'),
    url(r'^blog','blog.views.archive'),
    url(r'^contact','personalsite.views.contact'),
)
