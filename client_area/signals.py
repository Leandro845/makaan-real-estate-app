from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsLetter, NewsLetterContent


@receiver(post_save, sender=NewsLetterContent)
def send_newsletter_email(sender, instance, created, **kwargs):
    """
    A signal handler function triggered after saving a NewsLetterContent instance.
    Sends an email to all subscribers when new content is created.

    Args:
        sender (class): The model class from which the signal was sent (NewsLetterContent).
        instance (NewsLetterContent): The actual instance of NewsLetterContent that was saved.
        created (bool): Boolean indicating whether the instance was newly created or updated.
        **kwargs: Additional keyword arguments passed by the signal.

    """
    if created:
        # Get all email addresses from NewsLetter subscribers
        emails = NewsLetter.objects.values_list('email', flat=True)
        
        # Send email to each subscriber
        for email in emails:
            send_mail(
                '🔴 New content',  # Subject of the email
                instance.content,  # Content of the email
                settings.EMAIL_HOST_USER,  # Sender's email address
                [email],  # Recipient's email address
                fail_silently=False,  # Raise exceptions if email sending fails
            )
