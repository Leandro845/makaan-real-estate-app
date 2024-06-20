from django.contrib import admin  # Importing the admin module to use the Django admin interface
from django.urls import path, include  # Importing path and include functions to define URL patterns
from django.conf import settings  # Importing settings to access project settings
from django.conf.urls.static import static  # Importing static to serve static files during development

# urlpatterns is a list of URL patterns to route requests to the appropriate views
urlpatterns = [
    # Route for the Django admin interface
    path('admin/', admin.site.urls),
    
    # Route for the home page app, includes URL patterns defined in home_page.urls
    path('', include('home_page.urls')),
    
    # Route for the property app, includes URL patterns defined in property.urls
    path('property/', include('property.urls')),
    
    # Route for the client area app, includes URL patterns defined in client_area.urls
    path('client_area/', include('client_area.urls')),
    
    # Route for the custom 404 page app, includes URL patterns defined in page_not_found.urls
    path('page_not_found/', include('page_not_found.urls')),
    
    # Route for the authentication app, includes URL patterns defined in authenticate.urls
    path('auth/', include('authenticate.urls'))
] 
# Adding static file serving capabilities during development
# settings.MEDIA_URL is the URL to access media files
# settings.MEDIA_ROOT is the filesystem path to the directory that holds media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
