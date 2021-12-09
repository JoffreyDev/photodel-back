from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-m+%j26du1-)ga0fsdfdasrt245tbv4534fdsgxlw+aq5#()l+^(ecpdjnh-r_yoatm@o^'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'photodel',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '',
        'PORT': '5432',
    }
}

GDAL_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\gdal303.dll'
GEOS_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\geos_c.dll'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]