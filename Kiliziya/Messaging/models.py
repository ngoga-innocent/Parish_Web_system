from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000, unique=True)


class Messaging(models.Model):
    sender = models.CharField(max_length=10000)
    data = models.CharField(max_length=10000)
    reciever = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
