from django.contrib import admin
from .models import Messaging, Room
# Register your models here.


class Messages(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "data", "room", "status")


class Rooms(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "staff", "client",
                    "staff_pending", "client_pending")


admin.site.register(Messaging, Messages)
admin.site.register(Room, Rooms)
