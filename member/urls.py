__author__ = 'lyk-py'
from django.conf.urls import patterns, url, include

from member.views import (index, hakkimizda, register, hata, profil, tickets, logout, editprofil, newticket, ticketdetails)


urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^hakkimizda/$',hakkimizda),
                       url(r'^register/$', register),
                       url(r'^404/$', hata),
                       url(r'^profil/$', profil),
                       url(r'^tickets/$', tickets),
                       url(r'^logout/$', logout),
                       url(r'^editprofil/$', editprofil),
                       url(r'^new-ticket/$', newticket),
                       url(r'^ticket-detail/$', ticketdetails),

                       )