from django.urls import path
from . import views  # Import views from the current directory


urlpatterns = [
    # URL path for rendering the testimonial page
    path('testimonial/', views.testimonial, name='testimonial'),

    # URL paths for contact form handling
    path('contact/', views.contact, name='contact'),

    # URL path for handling newsletter subscription
    path('', views.newsletter, name='newsletter'),

    # URL paths for managing client account details
    path('my_account/<int:id>', views.my_account, name='my_account'),
    
    # URL path for deleting client account
    path('my_account/<int:id>/delete/', views.delete_account, name='delete_account'),

    # URL path for displaying and filtering client's properties
    path('my_properties_details/<int:id>', views.my_properties_details, name='my_properties_details')
]
