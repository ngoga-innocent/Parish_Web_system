from django.urls import path
from . import views
urlpatterns = [

    path('', views.Misa),
    path('Kongeramissa', views.ShyiramoMissa),


]
