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
    answered_tickets = list(set(Answer.objects.values_list("ticket_id", flat=True)))
    pool_tickets = Ticket.objects.exclude(id__in=answered_tickets)
    return render(request, 'index.html', locals())


def hakkimizda(request):
    return render_to_response('hakkimizda.html',context_instance=RequestContext(request))


def hata(request):
    return render_to_response('404.html', context_instance=RequestContext(request))


def tickets(request):
    if request.user.is_authenticated():
        user_details = UserDetails.objects.filter(user=request.user)[0]
        open_tickets = Ticket.objects.filter(user=request.user).filter(is_open=True)
        closed_tickets = Ticket.objects.filter(user=request.user).filter(is_open=False)
        return render(request, "tickets.html", locals())

    return HttpResponseRedirect('/login')


def ticketdetails(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket_answers = Answer.objects.filter(ticket_id=ticket_id)

    if request.method == 'POST':
        if request.POST.get("kapat"):
            t = ticket
            t.is_open = False
            t.save()
        else:
            try:
                answer = Answer()
                answer.user = request.user
                answer.content = request.POST.get('answercontent')
                answer.ticket_id = ticket
                answer.save()
                #return HttpResponseRedirect('/ticket-details')
            except Exception as e:
                print(e)
                return HttpResponseRedirect('/404')

    return render(request, "ticket-details.html", locals())


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
    #return render_to_response('register.html', context_instance=RequestContext(request))
    return render(request, "register.html", locals())


def profil(request):
    if request.user.is_authenticated():
        user_details = UserDetails.objects.filter(user=request.user)[0]
        open_tickets = Ticket.objects.filter(user=request.user).filter(is_open=True)
        closed_tickets = Ticket.objects.filter(user=request.user).filter(is_open=False)
        try:
            user_details = UserDetails.objects.filter(user=request.user)[0]
            return render(request,'profil.html', locals())

        except Exception as e:
            print(e)
            return HttpResponseRedirect('/404')


def editprofil(request):
    if request.user.is_authenticated():
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

        return render(request,'editprofil.html', locals())
    return HttpResponseRedirect('/login')


def newticket(request):
    if request.user.is_authenticated():
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

    return HttpResponseRedirect('/login')


