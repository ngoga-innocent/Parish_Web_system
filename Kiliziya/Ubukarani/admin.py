from django.contrib import admin
from .models import Icyangombwa, Ibyasabwe

# Register your models here.


class Ibyasa(admin.ModelAdmin):
    list_display = ("id", "amazina", "umubyeyi",
                    "umuryangoremezo", "status", "owner_id")


class Icyango(admin.ModelAdmin):
    list_display = ("id", "prenom", "Nom",
                    "papa", "mama", "parroise")


admin.site.register(Icyangombwa, Icyango)
admin.site.register(Ibyasabwe, Ibyasa)
