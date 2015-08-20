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
            user_detail = Member()
            user_detail.user = django_user
            user_detail.save()
            return HttpResponseRedirect('/login')
        except Exception as e:
            return HttpResponseRedirect('/login')
    return render_to_response('register.html', context_instance=RequestContext(request))


def profil(request):
    try:
        member = Member.objects.filter(user=request.user)[0]
        return render_to_response('profil.html', locals())
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/404')


def editprofil(request):
    try:
        if Member.objects.filter(user=request.user):
            member = Member.objects.filter(user=request.user)[0]
            return render_to_response('editprofil.html', locals())

        else:
            member = Member(user=request.user)

    except Exception as e:
        print(e)
        return HttpResponseRedirect('/404')


    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            twitter = request.POST.get('twitter')
            facebook = request.POST.get('facebook')
            github = request.POST.get('github')
            member.email = email
            member.linkedn = github
            member.twitter = twitter
            member.facebook = facebook
            request.user.save()
            member.save()
            return HttpResponseRedirect('/editprofil')
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/404')


    return render_to_response('editprofil.html', locals(), context_instance=RequestContext(request))