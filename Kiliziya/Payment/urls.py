from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Authorization, name='pay'),
    # path('cash_in', views.Pay, name='cashin'),

]
