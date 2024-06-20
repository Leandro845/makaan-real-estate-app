from django.db.models.signals import post_save  # Importing post_save signal
from django.dispatch import receiver  # Importing receiver decorator
from .models import Property  # Importing Property model from current module
from django.core.mail import send_mail  # Importing send_mail function from Django's email module
from django.conf import settings  # Importing settings from Django's configuration

@receiver(post_save, sender=Property)  # Receiver decorator for post_save signal, connected to Property model
def send_email_on_delete_property(sender, instance, created, **kwargs):
    if not created:
        # If the instance was not just created (i.e., it was updated or deleted)
        subject = 'Property Deleted'  # Subject of the email
        message = f'Property with id {instance.id} has been deleted'  # Message body of the email
        email_from = settings.EMAIL_HOST_USER  # Sender's email address (from Django settings)
        recipient_list = ['admin@example.com']  # List of recipient email addresses
        send_mail(subject, message, email_from, recipient_list)  # Send email using Django's send_mail function
        print('Email sent successfully')  # Print a success message to console
