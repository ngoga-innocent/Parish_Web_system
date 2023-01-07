from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('edit/<int:myid>', views.edit, name='edit')


]
