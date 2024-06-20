from django.apps import AppConfig


class ClientAreaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_area'

    def ready(self):
        import client_area.signals # Adjust this to match your actual app name