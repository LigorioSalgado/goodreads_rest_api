from .base import *
import os
import dj_database_url

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'NAME': os.getenv("DB_NAME"),
                         'USER': os.getenv("DB_USER"),
                         'PASSWORD': os.getenv("DB_PASSWORD"),
                         'HOST': 'localhost',
                         'PORT': '5432'
                         }
             }


#DATABASES = dict()

# DATABASES['default'] = dj_database_url.config()  # Heroku config

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = os.path.join(os.getcwd(), 'static')
