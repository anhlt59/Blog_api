# Django settings for local environment.
from .base import *


ALLOWED_HOSTS = ['*']


DEVELOPMENT_MODE = True
DEBUG = True
SECURE_SSL_REDIRECT = False


# config databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8001',
    'http://127.0.0.1:8000'
)
