# authenticate/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Client

class NameBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Attempt to retrieve a Client object by the provided username (name field)
        try:
            user = Client.objects.get(name=username)
        except Client.DoesNotExist:
            return None  # Return None if no Client with the provided username is found

        # Check if the retrieved user object exists and if the password matches
        if user and check_password(password, user.password):
            return user  # Return the user object if authentication is successful

        return None  # Return None if authentication fails

    def get_user(self, user_id):
        # Retrieve a Client object by its primary key (user_id)
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None  # Return None if no Client with the provided user_id is found
