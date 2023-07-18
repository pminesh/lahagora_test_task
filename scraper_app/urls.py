from django.urls import path
from scraper_app.views import GoogleAppStoreView
urlpatterns = [
    path('google_apps_store_details/', GoogleAppStoreView.as_view(),name='google-apps-store-details'),
]