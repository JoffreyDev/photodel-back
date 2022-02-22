import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photodel.settings')

app = Celery('photodel')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_transport_options = {"visibility_timeout": 604800}

app.autodiscover_tasks()

app.conf.CELERYBEAT_SCHEDULE = {
    'task_delete_last_views': {
        'task': 'tasks.items_task.task_delete_last_views',
        'schedule': crontab(hour=23, day_of_week='sunday'),
    }
}