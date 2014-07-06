__author__ = 'hguerrero'

from django.conf.urls import url, patterns

from relay import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^channel/(?P<channel_number>\d+)/$', views.turns_on_channel, name='turns_on_channel'), )