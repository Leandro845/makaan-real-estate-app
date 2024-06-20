from celery import shared_task
from django.core.mail import send_mail
from .models import NewsLetter


@shared_task
def sendmail(subject, message, host_mail, recipient_mail):
    """
    A Celery task to send an email asynchronously.

    Args:
        subject (str): Subject of the email.
        message (str): Content of the email.
        host_mail (str): Email address from which the email will be sent.
        recipient_mail (str): Email address of the recipient.
    """
    send_mail(
        subject,
        message,
        host_mail,
        [recipient_mail],
        fail_silently=False,
    )


@shared_task
def add_newsletter(email):
    """
    A Celery task to add an email to the newsletter list asynchronously.

    Args:
        email (str): Email address to be added to the newsletter list.

    Returns:
        int: ID of the NewsLetter object created.
    """
    newsLetter = NewsLetter.objects.create(email=email)
    return newsLetter.id
