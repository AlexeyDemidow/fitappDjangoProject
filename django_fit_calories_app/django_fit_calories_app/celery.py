import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fit_calories_app.settings')

app = Celery('django_fit_calories_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-message-at-9,12,15,18-hours': {
        'task': 'users.tasks.beat_mailing',
        'schedule': crontab(minute=0, hour='9,12,15,18'),
    },
}
