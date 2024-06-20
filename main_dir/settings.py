from pathlib import Path  # Module for object-oriented file system paths
from dotenv import load_dotenv  # Module to load environment variables from a .env file
import os  # Module providing a way of using operating system-dependent functionality
from django.contrib.messages import constants  # Module for constants used in Django messages framework
from django.contrib import messages  # Django's messages framework

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the project's root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is used for cryptographic signing
SECRET_KEY = 'django-insecure-!p#4zhm9-qg-6p1+it-z+it#zmxwm0)w=&m(7m27cqg3ql4!nl'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG mode is for development, should be False in production
DEBUG = True

# ALLOWED_HOSTS specifies a list of strings representing the host/domain names this Django site can serve
ALLOWED_HOSTS = ['*']

# Application definition

# INSTALLED_APPS is a list of all Django applications that are activated in this Django instance
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',  # Django app for storing Celery task results
    'django_ratelimit',  # Django app for rate limiting
    'django_redis',  # Django app for Redis cache backend
    'category',  # Custom app for categories
    'client_area',  # Custom app for client area
    'home_page',  # Custom app for home page
    'page_not_found',  # Custom app for 404 page
    'property',  # Custom app for properties
    'authenticate'  # Custom app for authentication
]

# MIDDLEWARE is a list of middleware to use
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.middleware.MyRateLimitMiddleware',  # Custom rate limiting middleware
]

# ROOT_URLCONF defines the module where the URL configurations are stored
ROOT_URLCONF = 'main_dir.urls'

# TEMPLATES is a list of configurations for the Django template system
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Specifies the template engine to use
        'DIRS': [Path(BASE_DIR, 'templates').joinpath()],  # Directories where Django will search for templates
        'APP_DIRS': True,  # Whether the template engine should look for templates inside installed applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION is the path to the WSGI application callable for serving the project
WSGI_APPLICATION = 'main_dir.wsgi.application'

# AUTHENTICATION_BACKENDS is a list of authentication backends to use
AUTHENTICATION_BACKENDS = [
    'authenticate.backends.NameBackend',  # Custom authentication backend
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

# CACHES configures the cache settings for the project
CACHES = {
    'default': {
        'BACKEND': os.environ['BACKEND'],  # Backend for caching
        'LOCATION': os.environ['LOCATION'],  # Location for the cache
        'OPTIONS': {
            'CLIENT_CLASS': os.environ['CLIENT_CLASS'],  # Client class for the cache
        }
    }
}

# Database configuration
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Load environment variables from a .env file
load_dotenv()

# DATABASES is a dictionary containing the settings for all databases to be used
DATABASES = {
    'default': {
        'ENGINE': os.environ['ENGINE'],  # Database engine to use
        'NAME': os.environ['DATABASE'],  # Name of the database
        'USER': os.environ['USER'],  # Database user
        'PASSWORD': os.environ['PASSWORD'],  # Database password
        'HOST': os.environ['HOST'],  # Database host
        'PORT': os.environ['PORT'],  # Database port
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS is a list of validators that are used to check the strength of user passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE is the language code for the project
LANGUAGE_CODE = 'en-us'

# TIME_ZONE is the time zone for the project
TIME_ZONE = 'UTC'

# USE_I18N enables Django’s translation system
USE_I18N = True

# USE_TZ enables timezone-aware datetimes
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL is the URL to use when referring to static files
STATIC_URL = 'static/'

# STATICFILES_DIRS is a list of filesystem directories to check when loading static files
STATICFILES_DIRS = [
    Path(BASE_DIR, 'templates/static').joinpath()
]

# MEDIA_ROOT is the absolute filesystem path to the directory that will hold user-uploaded files
MEDIA_ROOT = Path(BASE_DIR, 'media').joinpath()
# MEDIA_URL is the URL that handles the media served from MEDIA_ROOT
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD is the default field type for auto-generated primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages

# MESSAGE_TAGS is a dictionary that maps message levels to Bootstrap alert classes
MESSAGE_TAGS  = {
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success'
}

# Email

# EMAIL_BACKEND is the backend to use for sending emails
EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
# EMAIL_HOST is the host to use for sending emails
EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_PORT is the port to use for the email host
EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_USE_TLS specifies whether to use a TLS (secure) connection
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
# EMAIL_HOST_USER is the username to use for the email host
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD is the password to use for the email host
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# Celery

# CELERY_BROKER_URL is the URL of the message broker for Celery
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
# CELERY_RESULT_BACKEND is the backend to use for storing task results
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
# CELERY_ACCEPT_CONTENT specifies the content types that Celery will accept
CELERY_ACCEPT_CONTENT = os.environ['CELERY_ACCEPT_CONTENT']
# CELERY_RESULT_SERIALIZER specifies the serialization format for task results
CELERY_RESULT_SERIALIZER = os.environ['CELERY_RESULT_SERIALIZER']
# CELERY_TASK_SERIALIZER specifies the serialization format for tasks
CELERY_TASK_SERIALIZER = os.environ['CELERY_TASK_SERIALIZER']
# CELERY_WORKER_CONCURRENCY sets the number of concurrent worker processes
CELERY_WORKER_CONCURRENCY = os.environ['CELERY_WORKER_CONCURRENCY']
# CELERYD_MAX_TASKS_PER_CHILD sets the maximum number of tasks a worker can execute before being replaced
CELERYD_MAX_TASKS_PER_CHILD = os.environ['CELERYD_MAX_TASKS_PER_CHILD']
