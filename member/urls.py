__author__ = 'lyk-py'
from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                       url(r'^$', 'member.views.index'),
                       url(r'^hakkimizda/$', 'member.views.hakkimizda'),
                       url(r'^register/$', 'member.views.register'),
                       url(r'^404/$', 'member.views.hata'),
                       url(r'^profil/$', 'member.views.profil'),
                       url(r'^tickets/$', 'member.views.tickets'),
                       url(r'^logout/$', 'member.views.logout'),
                       )