from celery import shared_task
from django.contrib.auth.hashers import make_password
from .models import Client


@shared_task
def register(name, surname, email, password, confirm_password, address, phone, country, city, image, created_at, last_login):
    # Hash the passwords using Django's make_password function
    hashed_password = make_password(password)
    hashed_confirm_password = make_password(confirm_password)

    # Create a new Client instance with hashed passwords and other provided data
    client = Client(
        name=name,
        surname=surname,
        email=email,
        password=hashed_password,
        address=address,
        phone_number=phone,
        country=country,
        city=city,
        user_image=image,
        created_at=created_at,
        last_login=last_login
    )

    # Save the client instance to the database
    client.save()

    # Return the client's ID after saving
    return client.id
