# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from dashboard.models import Events, Subscribe

@receiver(post_save, sender=Events)
def send_event_notification(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscribe.objects.all()
        for subscriber in subscribers:
            send_mail(
                'New Event Created',
                f'A new event "{instance.Eventname}" has been created and will start on {instance.Start_date} at {instance.Start_time}.',
                'your-email@gmail.com',
                [subscriber.email],
                fail_silently=False,
            )

@receiver(post_save, sender=Subscribe)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to Our Event Website',
            'Thank you for subscribing to our event website. You will receive notifications about new events.',
            'your-email@gmail.com',
            [instance.email],
            fail_silently=False,
        )
