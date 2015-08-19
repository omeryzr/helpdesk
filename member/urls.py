__author__ = 'lyk-py'
from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                       url(r'^index/$', 'member.views.index'),
                       )