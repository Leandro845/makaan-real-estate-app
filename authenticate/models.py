from django.db import models
from django.contrib.auth.hashers import make_password, check_password as check_password_django


class Client(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True) 
    password = models.CharField(max_length=255)  # Storing hashed passwords
    address = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    user_image = models.ImageField(upload_to='img', null=True)  # Image upload field
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def is_authenticated(self):
        """Override Django's default is_authenticated method."""
        return True  # For custom authentication purposes

    def set_password(self, raw_password):
        """Set and save the hashed password for the client."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Check if the raw password matches the hashed password."""
        return check_password_django(raw_password, self.password)

    def __str__(self):
        """String representation of the Client instance."""
        return f'{self.name} {self.surname}'
