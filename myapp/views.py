from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from django.db.models.functions import ExtractMonth, ExtractDay

from dashboard.models import *

from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.

def Home(request):

    banner = Banner.objects.all()
    news = News.objects.all()
    feedback = Feedback.objects.all()
   

    to = timezone.now()
    today = to.date()
    cur_time = to.time()

    events = Events.objects.filter(
        Start_date__gt = today
    ).order_by('Start_date', 'Start_time')

    events_today = Events.objects.filter(
        Start_date = today, Start_time__gt = cur_time
    ).order_by('Start_date', 'Start_time')

    events = events | events_today

    now = datetime.now()
    upcoming_event = Events.objects.filter(
        Start_date__gt=now.date()
    ).order_by('Start_date', 'Start_time').first()

    if not upcoming_event:
        upcoming_event = Events.objects.filter(
            Start_date=now.date(),
            Start_time__gte=now.time()
        ).order_by('Start_date', 'Start_time').first()


    content = {'banner': banner, 'news': news, 'events': events, 'upcoming_event': upcoming_event, 'feedback': feedback, }

    return render(request, 'index.html', content)

def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscribe.objects.filter(email=email).exists():
                messages.info(request, 'You are already subscribed to our newsletter.')
            else:
                subscription = Subscribe(email=email)
                subscription.save()
                send_mail(
                    'Thank you for subscribing',
                    'Thank you for subscribing to our newsletter!',
                    'sunritculture@gmail.com', 
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('Home')
    return redirect('Home')

def About(request):
    feedback = Feedback.objects.all()
    content = {'feedback': feedback}
    
    return render(request, 'about.html', content)

def Upcoming(request):
    allevents = Events.objects.all()
    content = {'allevents': allevents}

    now = timezone.now()
    today = now.date()
    current_time = now.time()

    present_future_events = Events.objects.filter(
        Start_date__gt=today
    ).order_by('Start_date', 'Start_time')

    # Additionally, include events that start today but haven't started yet
    present_future_events_today = Events.objects.filter(
        Start_date=today, Start_time__gte=current_time
    ).order_by('Start_date', 'Start_time')

    present_future_events = present_future_events | present_future_events_today

    past_events = Events.objects.filter(
        Start_date__lt=today
    ).order_by('-Start_date', '-Start_time')

    
    past_events_today = Events.objects.filter(
        Start_date=today, Start_time__lt=current_time
    ).order_by('-Start_date', '-Start_time')

    past_events = past_events | past_events_today

    past_events_important = past_events.filter(Imp="Imp")
    past_events_not_important = past_events.filter(Imp="Not")

    context = {
        'present': present_future_events,
        'past_imp': past_events_important,
        'past_notimp': past_events_not_important,
    }


    return render(request, 'upcoming.html', context)

def Dance(request):
    galleries = Gallery.objects.all()

    events = Events.objects.filter(Category = 'Dance')

    content = {
        'galleries': galleries,
        'events': events,
    }

    return render(request, 'dance.html', content)

def Music(request):
    galleries = Gallery.objects.all()

    events = Events.objects.filter(Category = 'Music')

    content = {
        'galleries': galleries,
        'events': events,
    }
    return render(request, 'music.html', content)

def Arts(request):
    events = Events.objects.filter(Category = 'Arts')

    content = {
        'events': events,
    }
    return render(request, 'arts.html', content)

def Blog(request):
    blog = Blogs.objects.all()
    content = {'blog': blog}
    return render(request, 'blog.html', content)

def Galley(request):
    galleries = Gallery.objects.all()

    return render(request, 'gallery.html', {'galleries': galleries})

def Contct(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['email']
        sub = request.POST['sub']
        msg = request.POST['msg']

        record = Contact.objects.create(Name = name, Email = mail, Subject = sub, Message = msg)
        record.save()

        return redirect('Contact')

    return render(request, 'contact.html')

def Eventdetails(request, id):
    val = Events.objects.get(id = id)
    
    return render(request, 'eventdetails.html', {'val': val})

def Career(request):
    return render(request, 'career.html')

def Notice(request):
    return render(request, 'notice.html')

def Blogdetails(request):
    return render(request, 'blogdetails.html')

def Health(request):
    return render(request, 'health.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Terms(request):
    return render(request, 'terms.html')



