from django.db import models

class Housing(models.Model):
    name_housing = models.CharField(max_length=15)

    def __str__(self):
        return self.name_housing
    # This method returns a string representation of the model instance, 
    # which is useful for human-readable display in Django admin and elsewhere.

class Status(models.Model):
    name_status = models.CharField(max_length=15)

    def __str__(self):
        return self.name_status
    # Similarly, this method returns a string representation of the model instance.
