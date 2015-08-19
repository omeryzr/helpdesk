__author__ = 'lyk-py'
# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def hakkimizda(request):
    return render_to_response('hakkimizda.html',context_instance=RequestContext(request))
