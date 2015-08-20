from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    url = models.URLField()
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    photo = models.URLField(blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
            return self.user.username

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    is_open = models.BooleanField(default=True)
    category = models.ForeignKey('TicketCategory', related_name='tickets')

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    ticket_id = models.ForeignKey("Ticket", related_name="answers")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.username


class TicketCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ticket Category'
        verbose_name_plural = 'Ticket Categories'
