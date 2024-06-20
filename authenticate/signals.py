from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Client)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        # Send a welcome email when a new Client is created
        send_mail(
            'Welcome to our platform',
            'Thank you for registering with us. We are excited to have you on board.',
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )
    else:
        # Send an email when an existing Client's profile is updated
        send_mail(
            'Profile Updated',
            'Your profile has been updated.',
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )
