from pathlib import Path
import os
import datetime

BASE_URL = 'https://googletestphotodel.com/'

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.gis',

    'corsheaders',

    'rest_framework',
    'djoser',
    'django_cleanup.apps.CleanupConfig',
    'channels',

    'accounts',
    'additional_entities',
    'film_places',
    'gallery',
    'chat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'photodel.middleware.user_allow.UserVisit',
]

ROOT_URLCONF = 'photodel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
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


WSGI_APPLICATION = 'photodel.wsgi.application'
ASGI_APPLICATION = 'photodel.routing.application'


# To production
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'photodelru@mail.ru'
EMAIL_HOST_PASSWORD = 'H0ddpe5dTdq10Fjrmm7K'

# REDIS_HOST = '127.0.0.1'
REDIS_HOST = 'redis'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Etc/GMT-3'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSED": [
        'rest_framework.parsers.JSONParser',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ]
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=60),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}


INTERNAL_IPS = [
    '127.0.0.1',
]

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip2')


# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATIC FILES
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# MEDIA FILES
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'common': {
#             'format': '{levelname} {asctime} {name} message={message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'accountS_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs', 'accounts_debug.log'),
#             'formatter': 'common',
#             'backupCount': 10,
#             'maxBytes': 104857600,
#         },
#         'film_places_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs', 'film_places_debug.log'),
#             'formatter': 'common',
#             'backupCount': 10,
#             'maxBytes': 104857600,
#         },
#         'gallery_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs', 'gallery_debug.log'),
#             'formatter': 'common',
#             'backupCount': 10,
#             'maxBytes': 104857600,
#         },
#     },
#     'loggers': {
#         'accounts': {
#             'handlers': ['accountS_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'film_places': {
#             'handlers': ['film_places_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'gallery': {
#             'handlers': ['gallery_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     },
# }

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
