from django.shortcuts import render, redirect
from .tasks import register  # Importing asynchronous task for registration
from django.utils import timezone
from authenticate.models import Client
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants
from django.contrib import messages
from zxcvbn import zxcvbn  # Importing zxcvbn for password strength checking


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')  # Render registration form on GET request
    
    elif request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        image = request.POST.get('select_image')
        current_time = timezone.now()

        # Validate password strength using zxcvbn
        password_force = zxcvbn(password)
        if password_force['score'] < 3:
            messages.add_message(request, constants.ERROR, 'The password is weak.')
            return redirect('registration')  # Redirect if password is weak

        # Validate all required fields are filled
        if not all([name, surname, email, password, confirm_password, address, phone, country, city]):
            messages.add_message(request, constants.ERROR, 'All fields are required.')
            return redirect('registration')  # Redirect if any required field is missing
                
        # Check if password matches the confirmation
        if password != confirm_password:
            messages.add_message(request, constants.ERROR, 'Passwords do not match.')
            return redirect('registration')  # Redirect if passwords do not match

        # Validate password length
        if not (8 <= len(password) <= 16):
            messages.add_message(request, constants.ERROR, 'The password must be between 8 and 16 characters long.')
            return redirect('registration')  # Redirect if password length is invalid

        # Trigger asynchronous registration task
        register.delay(
            name, 
            surname,
            email,
            password,
            confirm_password,
            address,
            phone,
            country,
            city,
            image,
            current_time,
            current_time
        )
        
        return redirect('login')  # Redirect to login page after successful registration


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')  # Render login form on GET request

    elif request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        # Validate username and password fields
        if not username:
            messages.error(request, 'Username field is required.')
            return redirect('login')  # Redirect if username is missing

        if not password:
            messages.error(request, 'Password field is required.')
            return redirect('login')  # Redirect if password is missing

        try:
            user = Client.objects.get(name=username)
        except Client.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return redirect('login')  # Redirect if username does not exist

        # Validate password against stored hash
        if not user.check_password(password):
            messages.error(request, 'Incorrect password.')
            return redirect('login')  # Redirect if password is incorrect

        # Authenticate and login user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Authentication failed.')
            return redirect('login')  # Redirect if authentication fails


def logout_view(request):
    logout(request)  # Logout current user
    return redirect('home')  # Redirect to home page after logout
