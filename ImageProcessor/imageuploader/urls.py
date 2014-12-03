from django.conf.urls import patterns, include, url
from django.contrib import admin
from imageuploader.views import *

urlpatterns = patterns('',
    url(r'^$', PhotoList.as_view(), name='myphoto-list')
)    