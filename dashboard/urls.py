from django.contrib import admin
from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('login', Login, name='Login'),
    path('profile', Profile, name='Profile'),
    path('editprofile', Editprofile, name='Editprofile'),
    path('allevents', Allevents, name='Allevents'),
    path('addevent', AddEvent, name='AddEvent'),
    path('editevents/<int:id>/', Editevents, name='Editevents'),
    path('editevents/uprec/<int:id>/',uprec,name="uprec"),
    path('delete/<int:id>/',Delete ,name="delete"),
    path('news', Newss, name='News'),
    path('feedback', Feedbacks, name='Feedback'),
    path('banners', Banners, name='Banners'),
    path('addbanner', Addbanner, name='Addbanner'),
    path('blogs', Blog, name='Blogs'),
    path('addblog', Addblog, name='Addblog'),
    path('deleteblog/<int:id>/', Deleteblog, name='Deleteblog'),
    path('editbanner/<int:id>/', Editbanner, name='Editbanner'),
    path('dashboard', Dashboard, name='Dashboard'),
    path('useredit', Useredit, name='Useredit'),
    path('mainusers', Mainusers, name='Mainusers'),
    path('addgallery', Addgallery, name='Addgallery'),
    path('newuser', Newuser, name='Newuser'),
    path('logout', Logout, name='Logout'),
]
