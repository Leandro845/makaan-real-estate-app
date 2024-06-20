from django.contrib import admin
from .models import Housing, Status

class HousingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_housing')
    # Defines which fields are displayed in the admin list view for Housing.
    # 'id' and 'name_housing' are displayed as columns in the admin interface.

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_status')
    # Defines which fields are displayed in the admin list view for Status.
    # 'id' and 'name_status' are displayed as columns in the admin interface.

# Registers HousingAdmin and StatusAdmin with their respective models.
admin.site.register(Housing, HousingAdmin)
admin.site.register(Status, StatusAdmin)
