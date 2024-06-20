from django.shortcuts import render, get_object_or_404, redirect
from category.models import Housing, Status  # Importing Housing and Status models from category app
from authenticate.models import Client  # Importing Client model from authenticate app
from property.models import Property  # Importing Property model from property app
from django.core.paginator import Paginator  # Importing Paginator for pagination
from django.db.models import Q  # Importing Q object for complex queries
from django.contrib.auth.decorators import login_required  # Importing login_required decorator for views
from django.contrib.messages import constants  # Importing message constants
from django.contrib import messages  # Importing messages for user feedback
from django.http import HttpResponse  # Importing HttpResponse for HTTP responses
from .tasks import add  # Importing add task from local tasks module
from PIL import Image  # Importing Image from PIL library for image processing


def property_list(request):
    # View to list properties with optional status filtering and limit to 6 properties

    # Get the 'status' query parameter from the request
    filter_status = request.GET.get('status', None)

    # Retrieve all properties ordered by id descending
    properties_list = Property.objects.all().order_by('-id')

    # Filter properties by status if 'status' query parameter is present
    if filter_status:
        properties_list = properties_list.filter(status__name_status=filter_status)

    # Limit the number of properties to 6
    properties_list = properties_list[:6]

    # Return the queryset of properties
    return properties_list


def properties(request):
    # View to render the properties list page

    # Call property_list function to get the list of properties
    properties_list = property_list(request)

    # Render the 'property_list.html' template with properties_list context
    return render(request, 'property_list.html', {'properties_list': properties_list})


def count_properties_by_type():
    # Function to count properties for each housing type

    # List of housing types to count
    housing_types = ['Apartment', 'Villa', 'Home', 'Office', 'Building', 'Townhouse', 'Shop', 'Garage']

    # Empty list to store counts for each housing type
    property_counts = []

    # Loop through each housing type and count properties
    for housing_type in housing_types:
        count_ = Property.objects.filter(housing__name_housing=housing_type).count()
        property_counts.append(count_)

    # Return the list of property counts for each housing type
    return property_counts


def property_type(request):
    # View to render the property type page with counts of properties by type

    # Call count_properties_by_type function to get the counts of properties
    properties = count_properties_by_type()

    # Render the 'property_type.html' template with properties context
    return render(request, 'property_type.html', {'properties': properties})


def property_agent(request):
    # View to render the property agent page
    return render(request, 'property_agent.html')


def property_list_per_housing(request, type):
    # View to list properties filtered by housing type with search and pagination

    # Get the Housing object based on the 'type' parameter
    housing_type = Housing.objects.get(name_housing=type)

    # Get all Status objects
    status = Status.objects.all()

    # Get search term, property status, and location from POST data
    search_term = request.POST.get('search')
    property_status = request.POST.get('property_status')
    location = request.POST.get('location')

    # Filter properties by housing type and order by id descending
    properties_list = Property.objects.filter(housing=housing_type).order_by('-id')

    # Apply additional filters based on search term, property status, and location
    if search_term:
        properties_list = properties_list.filter(
            Q(status__name_status__icontains=search_term) |
            Q(address__icontains=search_term) |
            Q(street_number__icontains=search_term) |
            Q(city__icontains=search_term) |
            Q(country__icontains=search_term) |
            Q(property_listing__icontains=search_term)
        )

    elif property_status:
        properties_list = properties_list.filter(status__name_status=property_status)

    elif location:
        properties_list = properties_list.filter(city=location)

    # Create a Paginator object with 12 properties per page
    paginator = Paginator(properties_list, 12)

    # Get the page number from the GET parameters
    page_number = request.GET.get('page')

    # Get properties for the requested page
    properties_list = paginator.get_page(page_number)

    # Render the 'property_list_per_housing.html' template with context data
    return render(request, 'property_list_per_housing.html', {
        'obj_list': properties_list,
        'housing_type': housing_type,
        'status': status
    })


def details_property(request, id):
    # View to show details of a specific property identified by 'id'

    # Get the Property object with the given 'id'
    property = get_object_or_404(Property, id=id)

    # Render the 'details.html' template with property details context
    return render(request, 'details.html', {'property': property})


@login_required(login_url='login')
def add_property(request):
    # View to add a new property

    if request.method == 'GET':
        # If request method is GET, render the add property form

        # Get all Housing and Status objects
        housing = Housing.objects.all()
        status = Status.objects.all()

        # Render the 'add_property.html' template with housing and status context
        return render(request, 'add_property.html', {'housing': housing, 'status': status})

    elif request.method == 'POST':
        # If request method is POST, process the form data to add a new property

        # Get form data from POST request
        add_status = request.POST.get('status')
        add_housing = request.POST.get('housing')
        add_address = request.POST.get('address')
        add_street_number = request.POST.get('street_number')
        add_city = request.POST.get('city')
        add_country = request.POST.get('country')
        add_price = request.POST.get('price')
        add_description = request.POST.get('description')
        add_property_listing = request.POST.get('property_listing')
        add_image = request.FILES.get('select_image_property')
        add_sqft = request.POST.get('sqft')
        add_bathroom = request.POST.get('bathroom')
        add_badroom = request.POST.get('badroom')

        # Check if all required fields are filled
        required_fields = [
            add_status, add_housing, add_address, add_street_number,
            add_city, add_country, add_price, add_description,
            add_property_listing, add_image, add_sqft, add_bathroom, add_badroom
        ]
        if not all(required_fields):
            # If any required field is missing, show an error message
            messages.error(request, 'Please fill all fields')
            return redirect('add_property')

        try:
            # Convert price, sqft, bathroom, and bedroom values to appropriate types
            add_price = float(add_price)
            add_sqft = int(add_sqft)
            add_bathroom = int(add_bathroom)
            add_badroom = int(add_badroom)
        except ValueError:
            # If conversion fails, show an error message
            messages.error(request, 'Please provide valid numeric values for price, sqft, bathroom, and bedroom.')
            return redirect('add_property')

        try:
            # Open and resize the image, then save it to 'media/' directory
            image = Image.open(add_image)
            image = image.resize((600, 400))
            image_filename = add_image.name
            image.save('media/' + image_filename)
        except Exception as e:
            # If image processing fails, show an error message
            messages.error(request, f'Error saving image: {e}')
            return redirect('add_property')

        try:
            # Get Status and Housing objects based on form data
            status = Status.objects.get(name_status=add_status)
            housing = Housing.objects.get(name_housing=add_housing)
        except Status.DoesNotExist:
            # If selected status does not exist, show an error message
            messages.error(request, 'Selected status does not exist')
            return redirect('add_property')
        except Housing.DoesNotExist:
            # If selected housing type does not exist, show an error message
            messages.error(request, 'Selected housing type does not exist')
            return redirect('add_property')

        # Create a new Property object with form data and save it to the database
        property = Property(
            client=request.user,  # Assuming request.user is the logged-in user
            status=status,
            housing=housing,
            address=add_address,
            street_number=add_street_number,
            city=add_city,
            country=add_country,
            price=add_price,
            description=add_description,
            property_listing=add_property_listing,
            image=image_filename,
            sqft=add_sqft,
            bath=add_bathroom,
            bad=add_badroom
        )
        property.save()

        # Call the add task asynchronously to process the new property
        add.delay(property.id)

        # Show a success message and redirect to the add property page
        messages.success(request, 'Property added successfully')
        return redirect('add_property')


def delete_property(request, id):
    # View to delete a property identified by 'id'

    if request.method == 'POST':
        # If request method is POST, delete the property with the given 'id'
        property = Property.objects.get(id=id)
        property.delete()

        # Return an HTTP response (not typically returning 'home' directly)
        return HttpResponse('home')

        # Consider redirecting to a specific URL or rendering a template after deletion

