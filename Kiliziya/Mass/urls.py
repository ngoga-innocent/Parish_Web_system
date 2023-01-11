from django.urls import path
from . import views
urlpatterns = [

    path('', views.Misa, name="missa"),
    path('Kongeramissa', views.ShyiramoMissa, name="new_mass"),
    path('<int:myid>', views.Mass_detail, name='mass_detail')


]
