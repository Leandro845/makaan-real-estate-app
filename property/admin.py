from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    # Define which fields are displayed in the admin list view
    list_display = ('id', 'descri')

# Register the Property model with the custom PropertyAdmin configuration
admin.site.register(Property, PropertyAdmin)
