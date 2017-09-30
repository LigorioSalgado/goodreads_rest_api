from .base import *
import os
import dj_database_url

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = dict()

DATABASES['default'] = dj_database_url.config()  # Heroku config

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = os.path.join(os.getcwd(), 'static')
