from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('ubukarani/', include('Ubukarani.urls')),
    path('announcements/', include('Announcements.urls')),
    path('Mass/', include('Mass.urls')),
    path('Event/', include('Events.urls')),
    path('User/', include('User.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
