from django.db import models
# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    url = models.URLField()
    twitter = models.URLField()
    github = models.URLField()
    facebook = models.URLField()

    def __print__(self):
            return self.username


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    ticket_member = models.ForeignKey('Member', related_name="tickets")
    is_open = models.BooleanField(default=True)
    category = models.ForeignKey('TicketCategory', related_name='tickets')

    def __print__(self):
        return self.title


class Answers(models.Model):
    member = models.ForeignKey("Member", related_name="answers")
    content = models.TextField()
    ticket_id = models.ForeignKey("Ticket", related_name="answers")
    create_date = models.DateTimeField(auto_now_add=True)

    def __print__(self):
        return self.member.username


class TicketCategory(models.Model):
    name = models.TextField(max_length=60)

    def __print__(self):
        return self.name
