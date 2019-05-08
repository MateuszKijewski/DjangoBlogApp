from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="home"),
    path('about', views.About, name="about"),
    path('contact', views.Contact, name="contact"),
    path('add', views.Add_post, name="add"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)