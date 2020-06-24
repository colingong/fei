from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from share.config_celery_broker import REDIS_BROKER_FOR_CELERY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_settings.settings')

# app = Celery('fei', broker=REDIS_BROKER_FOR_CELERY)
app = Celery('fei')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = REDIS_BROKER_FOR_CELERY

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
