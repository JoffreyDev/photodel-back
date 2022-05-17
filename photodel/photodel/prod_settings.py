from pathlib import Path

import datetime
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-m+%j26du1-)ga03596dfg4534fdsgxlw+aq5#()l+^(ecpdjnh-r_yoatm@o^'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '34.116.234.236', 'googletestphotodel.com', 'photodel.ru', ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:8000',
# ]
# CORS_ORIGIN_REGEX_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:8000',
# ]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'photodeldb',
        # 'NAME': 'photodel',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '',
        # 'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]