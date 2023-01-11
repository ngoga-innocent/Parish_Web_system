from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Home, name='staff'),
    path('pending', views.Pending, name='pending'),
    path('approve/<int:id>', views.Approve, name='approve'),
    path('view/<int:id>', views.Review, name='review')

]
