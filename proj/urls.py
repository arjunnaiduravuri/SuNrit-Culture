"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('subscribe/', subscribe_view, name='subscribe'),
    path('about', About, name='About'),
    path('upcoming', Upcoming, name='Upcoming'),
    path('dance', Dance, name='Dance'),
    path('music', Music, name='Music'),
    path('arts', Arts, name='Arts'),
    path('blog/', Blog, name='Blog'),
    path('gallery', Galley, name='Gallery'),
    path('contact', Contct, name='Contact'),
    path('eventdetails/<int:id>/', Eventdetails, name='Eventdetails'),
    path('career', Career, name='Career'),
    path('notice', Notice, name='Notice'),
    path('blogdetails', Blogdetails, name='Blogdetails'),
    path('health', Health, name='Health'),
    path('privacy', Privacy, name='Privacy'),
    path('terms', Terms, name='Terms'),
    path('', include('dashboard.urls')),
    # path('profile', Admin, name='Admin'),
    # path('editprofile', Editprofile, name='Editprofile'),
    # path('viewprofile', Viewinguser, name='Viewinguser'),
    # path('addnew', Addnew, name='Addnew'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)