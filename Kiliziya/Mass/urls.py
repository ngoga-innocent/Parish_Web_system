from django.urls import path
from . import views
urlpatterns = [

    path('', views.Misa),
    path('Kongeramissa', views.ShyiramoMissa),
    path('<int:myid>', views.Mass_detail, name='mass_detail')


]
