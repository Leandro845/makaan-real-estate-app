from django.shortcuts import render
from django.http import HttpResponse
from property.views import count_properties_by_type  # Importing function from property.views
from property.views import property_list  # Importing function from property.views
from authenticate.models import Client  # Importing Client model from authenticate app models

def home(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Call count_properties_by_type function to get properties count by type
        properties = count_properties_by_type()
        # Call property_list view to get properties list based on request
        properties_list = property_list(request)
        # Render home.html template with properties and properties_list context
        return render(request, 'home.html', {'properties': properties, 'properties_list': properties_list})
    else:
        # If user is not authenticated, render home.html with empty properties and properties_list context
        return render(request, 'home.html', {'properties': None, 'properties_list': None})

def about(request):
    # Render about.html template
    return render(request, 'about.html')
