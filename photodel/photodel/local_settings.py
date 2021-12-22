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

if os.name == 'nt':
    OSGEO4W = r"C:\OSGeo4W"
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = "C:\Program Files\GDAL\gdal-data"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal303.dll'
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

GEOS_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\geos_c.dll'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]