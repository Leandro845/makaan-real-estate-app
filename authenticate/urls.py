from django.urls import path
from . import views  # Importing views from the current directory


urlpatterns = [
    path('registration/', views.registration, name='registration'),  # URL pattern for registration view
    path('login/', views.login_view, name='login'),  # URL pattern for login view
    path('logout/', views.logout_view, name='logout'),  # URL pattern for logout view
]
