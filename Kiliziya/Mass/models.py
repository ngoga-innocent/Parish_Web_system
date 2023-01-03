from django.db import models

# Create your models here.


class Mass(models.Model):
    time = models.CharField(max_length=7)
    place = models.CharField(max_length=50)
    padiri = models.CharField(max_length=50)
    verse_1 = models.CharField(max_length=100)
    isomo_1 = models.TextField()
    verse_2 = models.CharField(max_length=100)
    isomo_2 = models.TextField()
    ivanjiri_verse = models.CharField(max_length=100)
    ivanjiri = models.TextField()
    summary = models.TextField()
    umwanzuro = models.TextField()
