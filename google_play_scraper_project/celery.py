import os

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google_play_scraper_project.settings')

celery_app = Celery('google_play_scraper_project')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

