from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Rooms, name='chat'),
    path('<int:id>', views.ChatRoom, name='chat_room'),

]
