import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photodel.settings')

app = Celery('photodel')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_transport_options = {"visibility_timeout": 604800}

app.autodiscover_tasks()

app.conf.CELERYBEAT_SCHEDULE = {
    'task_delete_views': {
        'task': 'tasks.accounts_task.task_delete_last_views',
        'schedule': crontab(hour=0, day_of_week='sunday'),
    },

    'task_update_current_ad': {
        'task': 'tasks.accounts_task.task_update_current_ad',
        'schedule': 300,
    },

    'task_update_profile_likes': {
        'task': 'tasks.accounts_task.task_update_profile_likes',
        'schedule': crontab(hour=0),
    },

    'task_update_place_likes': {
        'task': 'tasks.accounts_task.task_update_place_likes',
        'schedule': crontab(hour=0),
    },

    'task_update_photos_likes': {
        'task': 'tasks.accounts_task.task_update_photos_likes',
        'schedule': crontab(hour=0),
    },

    'check_ads_dates': {
        'task': 'tasks.accounts_task.check_ads_dates',
        'schedule': crontab(hour=0),
    },

    'reset_temp_location': {
        'task': 'tasks.accounts_task.reset_temp_location',
        'schedule': crontab(hour=0),
    },

}
