from celery import Celery  # Importing Celery class for task queue implementation
import os  # Importing os module for operating system interactions

# Setting the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_dir.settings')

# Creating an instance of Celery and naming it 'main_dir'
app = Celery('main_dir')

# Loading configuration from the Django settings, looking for keys with the prefix 'CELERY'
app.config_from_object('django.conf.settings', namespace='CELERY')

# Automatically discovering tasks from all installed apps that have a tasks.py file
app.autodiscover_tasks()

# Defining a sample task for debugging purposes
@app.task(bind=True)  # The bind=True argument allows the task to access its own instance as 'self'
def debug_task(self):
    # Printing the request object of the task, useful for debugging
    print(f'Request: {self.request!r}')
