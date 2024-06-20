from celery import shared_task  # Importing shared_task decorator from Celery
from .models import Property  # Importing Property model from the current module
from django.core.mail import send_mail  # Importing send_mail function from Django's email module
from django.conf import settings  # Importing settings from Django's configuration

@shared_task  # Decorator to mark this function as a Celery task
def add(property_id):
    try:
        # Attempt to retrieve the Property object using the provided property_id
        property = Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        # Handle the case where the Property with the given ID does not exist
        print(f"Property with ID {property_id} not found.")
        return  # Exit the function if the Property does not exist

    # Send a confirmation email
    try:
        send_mail(
            'Property Added Successfully',  # Subject of the email
            f'Your property has been added successfully!',  # Message body of the email
            settings.EMAIL_HOST_USER,  # Sender's email address (from Django settings)
            [property.client.email],  # List of recipient email addresses
            fail_silently=False,  # Raise an exception if the email sending fails
        )
        print(f"Confirmation email sent to {property.client.email}")  # Print a success message to console
    except Exception as e:
        print(f"Error sending email: {e}")  # Print an error message if sending email fails

    print(f"Asynchronous task completed for property {property.id}")  # Print a completion message to console
