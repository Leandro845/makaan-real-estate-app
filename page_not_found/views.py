from django.shortcuts import render
from django.conf.urls import handler404


def page_not_found(request):
    """
    A custom view function to handle 404 errors.

    This function renders a custom 404.html template when a page is not found.

    Args:
    - request: HttpRequest object representing the request made to the server.

    Returns:
    - HttpResponse object that renders the 404.html template.

    Notes:
    - This function is intended to be used as a handler for 404 errors in Django.
    - It uses Django's render function to render the 404.html template with the request context.
    """
    return render(request, '404.html')

handler404 = page_not_found
