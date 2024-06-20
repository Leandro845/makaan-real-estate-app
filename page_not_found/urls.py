from django.urls import path
from . import views

# Define the urlpatterns list which maps URL patterns to view functions or classes
urlpatterns = [
    # Define a path for the root URL (''), which typically corresponds to the base URL of your application
    path('', views.page_not_found, name='page_not_found'),  # This maps the root URL to the page_not_found view function
]
