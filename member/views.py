__author__ = 'lyk-py'
# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from member.models import Member

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def hakkimizda(request):
    return render_to_response('hakkimizda.html',context_instance=RequestContext(request))


def hata(request):
    return render_to_response('404.html', context_instance=RequestContext(request))


def tickets(request):
    return render_to_response('tickets.html', context_instance=RequestContext(request))


def profil(request):
    return render_to_response('profil.html', context_instance=RequestContext(request))


def logout(request):
    return render_to_response('logout.html', context_instance=RequestContext(request))


def editprofil(request):
    return render_to_response('editprofil.html', context_instance=RequestContext(request))




def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            django_user = User.objects.create_user(username, email, password)
            user_detail = Member(username=username)
            user_detail.user = django_user
            user_detail.save()
            return HttpResponseRedirect('/login')
        except Exception as e:
            return HttpResponseRedirect('/login')
    return render_to_response('register.html', context_instance=RequestContext(request))


def profil(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        return render_to_response('profil.html', locals())
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/404')


def editprofile(request):
    try:
        if Member.objects.filter(username=request.user.username):
            member = Member.objects.filter(username=request.user.username)[0]

        else:
            member = Member(username=request.user.username)
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/sorry')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            twitter = request.POST.get('twitter')
            facebook = request.POST.get('facebook')
            github = request.POST.get('github')
            member_user_auth = User.objects.create_user(username, password, email)
            member_user_auth.save()
            mmbr = Member(first_name=name, surname=surname, email=email, twitter=twitter, facebook=facebook, github=github)
            mmbr.save()
            return HttpResponseRedirect('/login')
        except Exception as e:
            return HttpResponseRedirect('/login')
    return render_to_response('register.html', context_instance=RequestContext(request))