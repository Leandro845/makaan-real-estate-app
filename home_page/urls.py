from django.urls import path  # Import path function from django.urls
from . import views  # Import views module from the current directory (assuming views.py exists here)

urlpatterns = [
    path('', views.home, name='home'),    # URL pattern for the home view
    path('about/', views.about, name='about')  # URL pattern for the about view
]
