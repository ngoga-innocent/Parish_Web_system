from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000)
    staff = models.CharField(max_length=10000, null=True)
    client = models.CharField(max_length=10000, null=True)
    staff_pending = models.IntegerField(null=True, default=0)
    client_pending = models.IntegerField(null=True, default=0)


class Messaging(models.Model):
    Status_choices = {
        ('1', 'not read'),
        ('2', 'read')
    }
    sender = models.CharField(max_length=10000, null=True)
    data = models.CharField(max_length=10000)
    room = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=10000, null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status_choices,
        default='1'
    )
