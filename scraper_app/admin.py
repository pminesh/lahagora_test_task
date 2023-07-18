from django.contrib import admin
from scraper_app import models as scraper_models

admin.site.register(scraper_models.AppDetails)
admin.site.register(scraper_models.Developer)