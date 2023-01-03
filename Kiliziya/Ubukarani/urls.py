from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.Home),
    path('kwiyandikisha', views.Register),
    path('icyemezo', views.icyemezo, name="ibyemezo"),
    path('icyangombwa/<int:id>/', views.icyemezo_detail, name='icyangombwa '),
]
