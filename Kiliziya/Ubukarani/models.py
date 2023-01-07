from django.db import models

# Create your models here.


class Icyangombwa(models.Model):
    amazina = models.CharField(max_length=200)
    papa = models.CharField(max_length=200)
    mama = models.CharField(max_length=200)
    umubyeyi_wa_batisimu = models.CharField(max_length=200)
    parroise = models.CharField(max_length=200)
    itariki_yamavuko = models.DateField()
    batisimu = models.DateField()
    Ukaristiya = models.DateField()
    Gukomezwa = models.DateField()
    batisimu_status = models.BooleanField(default=False)
    Ukaristiya_status = models.BooleanField(default=False)
    Gukomezwa_status = models.BooleanField(default=False)


class Ibyasabwe(models.Model):

    Status_choices = {
        ('1', 'Pending'),
        ('2', 'approved')
    }
    amazina = models.CharField(max_length=1000)
    umubyeyi = models.ImageField(upload_to='pics')
    umuryangoremezo = models.ImageField(upload_to='pics')
    status = models.CharField(
        max_length=20,
        choices=Status_choices,
        default='1'
    )
