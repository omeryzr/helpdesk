from django.db import models

# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.username

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    release_date = models.DateField()
    ticket_member = models.ForeignKey('Member', related_name="tickets")