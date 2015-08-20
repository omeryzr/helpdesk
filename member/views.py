__author__ = 'lyk-py'
# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from member.models import UserDetails, TicketCategory, Ticket, Answer
from django.template.context_processors import csrf

# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def hakkimizda(request):
    return render_to_response('hakkimizda.html',context_instance=RequestContext(request))


def hata(request):
    return render_to_response('404.html', context_instance=RequestContext(request))


def tickets(request):
    user_details = UserDetails.objects.filter(user=request.user)[0]
    open_tickets = Ticket.objects.filter(user=request.user).filter(is_open=True)
    closed_tickets = Ticket.objects.filter(user=request.user).filter(is_open=False)

    return render(request, "tickets.html", locals())


def profil(request):
    return render_to_response('profil.html', context_instance=RequestContext(request))


def logout(request):
    return render_to_response('logout.html', context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            django_user = User.objects.create_user(username, email, password)
            user_detail = UserDetails()
            user_detail.user = django_user
            user_detail.save()
            return HttpResponseRedirect('/login')
        except Exception as e:
            return HttpResponseRedirect('/login')
    return render_to_response('register.html', context_instance=RequestContext(request))


def profil(request):
    try:
        user_details = UserDetails.objects.filter(user=request.user)[0]
        return render_to_response('profil.html', locals())
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/404')


def editprofil(request):
    if UserDetails.objects.filter(user=request.user).exists():
        user_details = UserDetails.objects.filter(user=request.user)[0]
    if request.method == 'POST':
        try:
            user = request.user
            user.email = request.POST.get('email')
            user.first_name = request.POST.get('name')
            user.last_name = request.POST.get('surname')
            user.save()
            user_details.url = request.POST.get('url')
            user_details.github = request.POST.get('github')
            user_details.twitter = request.POST.get('twitter')
            user_details.facebook = request.POST.get('facebook')
            user_details.save()

            return HttpResponseRedirect('/profil')

        except Exception as e:
            print(e)
            return HttpResponseRedirect('/404')

    return render_to_response('editprofil.html',RequestContext(request, locals()))


def newticket(request):
    user_details = UserDetails.objects.get(user=request.user)
    ticket_categories = TicketCategory.objects.all()

    if request.method == 'POST':
        try:
            t = Ticket()
            t.title = request.POST.get("title")
            t.content = request.POST.get("content")
            t.user = request.user
            t.category = TicketCategory.objects.filter(name = request.POST.get("ticketcategory"))[0]
            t.save()
            return HttpResponseRedirect('/profil')


        except Exception as e:
            #return HttpResponseRedirect('/404')
            return render(request, "new-ticket.html", locals())

    return render(request, "new-ticket.html", locals())
