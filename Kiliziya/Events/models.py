from django.db import models

# Create your models here.


class Event(models.Model):
    thumb = models.ImageField(upload_to='pics', null=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
