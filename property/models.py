from django.db import models  # Importing Django's models module
from category.models import Housing, Status  # Importing Housing and Status models from category app
from authenticate.models import Client  # Importing Client model from authenticate app

class Property(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    street_number = models.IntegerField()
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    property_listing = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')  # ImageField for property images, uploaded to 'img' directory

    sqft = models.IntegerField()  # Square footage of the property
    bath = models.IntegerField()  # Number of bathrooms
    bad = models.IntegerField()   # Number of bedrooms

    def descri(self):
        return f'{self.property_listing} {self.city}'



    
    

