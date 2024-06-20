from django.contrib import admin
from .models import NewsLetter, NewsLetterContent

# Admin class for NewsLetter model
class AdminNewsLetter(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')  # Fields displayed in the admin list view

# Registering NewsLetter model with AdminNewsLetter configuration
admin.site.register(NewsLetter, AdminNewsLetter)

# Admin class for NewsLetterContent model
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Fields displayed in the admin list view

# Registering NewsLetterContent model with ContentAdmin configuration
admin.site.register(NewsLetterContent, ContentAdmin)
