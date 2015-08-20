from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    url = models.URLField()
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    photo = models.URLField(blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
            return self.user.username


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    ticket_member = models.ForeignKey('Member', related_name="tickets")
    is_open = models.BooleanField(default=True)
    category = models.ForeignKey('TicketCategory', related_name='tickets')

    def __str__(self):
        return self.title


class Answer(models.Model):
    member = models.ForeignKey("Member", related_name="answers")
    content = models.TextField()
    ticket_id = models.ForeignKey("Ticket", related_name="answers")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.username


class TicketCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


# def newticket(request):
#     if Member.objects.filter(user=request.user).exists():
#         member = Member.objects.filter(user=request.user)[0]
#         ticket = Ticket.objects.filter(ticket_member=request.user)[0]
#     if request.method == 'POST':
#         try:
#             ticket.title = request.POST.get('title')
#             ticket.content = request.POST.get('content')
#             ticket.ticketcategory = 1
#             ticket.save()
#             return HttpResponseRedirect('/profil')
#
#         except Exception as e:
#             print(e)
#             return HttpResponseRedirect('/404')
#
#     return render_to_response('new-ticket.html', RequestContext(request, locals()))