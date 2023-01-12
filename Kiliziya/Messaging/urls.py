from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Home, name='chat'),
    path('staff/<int:id>', views.StaffCheck, name='staffchek'),
    path('<int:id>', views.ChatRoom, name='chat_room'),

]
