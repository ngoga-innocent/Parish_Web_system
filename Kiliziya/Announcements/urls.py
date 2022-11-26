from django.urls import path
from . import views
urlpatterns = [

    path('', views.Announcement),
    path('<int:id>/', views.Announcement_detail, name='announcements_detail'),
    path('create', views.CreateAnnouncements)
]
