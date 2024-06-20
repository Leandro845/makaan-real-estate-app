from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models import Q
from .tasks import sendmail, add_newsletter  # Importing tasks from the same module
from authenticate.models import Client
from property.models import Property
import bcrypt
from category.models import Housing, Status

# View for rendering the testimonial page
def testimonial(request):
    return render(request, 'testimonial.html')

# View for handling contact form submissions
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    elif request.method == 'POST':
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate form inputs
        if not all([name, email, subject, message]):
            messages.add_message(request, constants.ERROR, 'Please fill in all fields')
            return redirect('contact')

        try:
            # Send email using a background task
            sendmail(
                f'{name} - {subject}',
                message,
                email,
                'le.junior2003@gmail.com'
            )
            messages.add_message(request, constants.SUCCESS, 'Email sent successfully')
            return redirect('contact')
        except:
            messages.add_message(request, constants.ERROR, 'Error sending email')
            return redirect('contact')

# View for handling newsletter subscription
def newsletter(request):
    if request.method == 'GET':
        return redirect(request.META.get('HTTP_REFERER', '/'))
    elif request.method == 'POST':
        email = request.POST.get('email')
        add_newsletter(email)  # Add email to newsletter list
        return redirect(request.META.get('HTTP_REFERER', '/'))

# View for rendering and updating client account details
def my_account(request, id):
    client = Client.objects.get(id=id)  # Retrieve client object by ID

    if request.method == 'GET':
        return render(request, 'my_account.html', {'client': client})
    elif request.method == 'POST':
        # Mapping form fields to Client model attributes
        field_mapping = {
            'email_update': 'email',
            'password_update': 'password',
            'address_update': 'address',
            'phone_number_update': 'phone_number',
            'country_update': 'country',
            'city_update': 'city',
        }

        # Update client fields based on form data
        for field_name, model_attribute in field_mapping.items():
            if field_name in request.POST:
                # Encrypt password using bcrypt
                if model_attribute == 'password':
                    client.password = bcrypt.hashpw(request.POST[field_name].encode(), bcrypt.gensalt()).decode()
                else:
                    setattr(client, model_attribute, request.POST[field_name])

        # Handle image upload (if any)
        if 'user_image' in request.FILES:
            client.user_image = request.FILES['user_image']

        try:
            client.save()  # Save updated client data
            messages.success(request, 'Account successfully updated.')
            return redirect('my_account', id=id)
        except:
            messages.error(request, 'An error occurred while updating your account')
            return redirect('my_account', id=id)

# View for deleting client account
def delete_account(request, id):
    if request.method == 'POST':
        client = Client.objects.get(id=id)
        client.delete()  # Delete client account

    return redirect('home')

# View for displaying and filtering client's properties
def my_properties_details(request, id):
    client = get_object_or_404(Client, pk=id)  # Retrieve client object by ID
    my_properties = Property.objects.filter(client=client).order_by('-id')  # Filter properties by client and order by ID

    # Handle search, status filter, and location filter
    search_term = request.POST.get('search')
    property_status = request.POST.get('property_status')
    location = request.POST.get('location')

    if search_term:
        # Filter properties by search term
        my_properties = my_properties.filter(
            Q(status__name_status__icontains=search_term) |
            Q(address__icontains=search_term) |
            Q(street_number__icontains=search_term) |
            Q(city__icontains=search_term) |
            Q(country__icontains=search_term) |
            Q(property_listing__icontains=search_term)
        )
    elif property_status:
        # Filter properties by status and client
        my_properties = my_properties.filter(status__name_status=property_status).filter(client=client)
    elif location:
        # Filter properties by location and client
        my_properties = my_properties.filter(city=location).filter(client=client)

    paginator = Paginator(my_properties, 12)  # Pagination: 12 items per page
    page_number = request.GET.get('page')
    my_properties = paginator.get_page(page_number)

    return render(request, 'my_properties.html', {
        'obj_list': my_properties
    })
