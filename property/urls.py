from django.urls import path  # Importing path function from django.urls
from . import views  # Importing views from the current module (assuming views.py)

# URL patterns for property-related views
urlpatterns = [
    # URL pattern for listing properties
    path('property_list/', views.properties, name='property_list'),
    
    # URL pattern for displaying property types and counts
    path('property_type/', views.property_type, name='property_type'),
    
    # URL pattern for property agent page
    path('property_agent/', views.property_agent, name='property_agent'),
    
    # URL pattern for listing properties based on housing type
    path('property_list_per_housing/<str:type>', views.property_list_per_housing, name='property_list_per_housing'),
    
    # URL pattern for displaying details of a specific property by ID
    path('detail_property/<int:id>', views.details_property, name='details_property'),
    
    # URL pattern for adding a new property
    path('add_property/', views.add_property, name='add_property'),
    
    # URL pattern for deleting a property by ID
    path('delete_property/<int:id>', views.delete_property, name='delete_property'),
]

