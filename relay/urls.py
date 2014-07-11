__author__ = 'hguerrero'

from django.conf.urls import url, patterns

from relay import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^channel/(?P<channel_number>\d+)/$', views.toggle_channel_sync, name='turns_on_channel'),
                       url(r'^channel/ajax/(?P<channel_number>\d+)/$', views.toggle_channel_async, name='toggle_channel'))