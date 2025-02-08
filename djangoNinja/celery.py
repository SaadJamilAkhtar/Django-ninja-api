import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoNinja.settings")

app = Celery("djangoNinja")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
