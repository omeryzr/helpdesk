from django.db import models

# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
