import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photodel.settings')

app = Celery('photodel')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_transport_options = {"visibility_timeout": 86400}

app.autodiscover_tasks()