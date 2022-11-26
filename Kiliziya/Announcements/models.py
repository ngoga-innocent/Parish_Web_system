from django.db import models

# Create your models here.


class Announcements(models.Model):
    thumb = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=300)
    description = models.TextField()
