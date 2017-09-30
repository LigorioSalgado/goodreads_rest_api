from .base import *

SECRET_KEY = '-o^f2!yq436m=&+*_gcbhv^gs4sp5r--2x!hc4_))f68u!=ffd'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'NAME': 'good_db',
                         'USER': 'admin_good',
                         'PASSWORD': 'good2017',
                         'HOST': 'localhost',
                         'PORT': '5432'
                         }
             }
