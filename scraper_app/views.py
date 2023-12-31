from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scraper_app import tasks as scraper_task
from scraper_app import models as scraper_models
from scraper_app.serializers import AppDetailsSerializer

class GoogleAppStoreView(APIView):
    """
    API view to fetch and store Google Play Store app details.
    """
    def get(self, request):
        """
        GET request handler to fetch all Google Play Store app details.
        """
        all_apps_data = scraper_models.AppDetails.objects.all()
        serializer = AppDetailsSerializer(all_apps_data,many=True)
        return Response({"google_apps_data":serializer.data},status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        POST request handler to initiate scraping of Google Play Store app details.
        """
        url = request.data.get("url")
        lang = request.data.get("lang")
        country = request.data.get("country")

        data = {"url":url,"lang":lang,"country":country}
        scraper_task.store_google_play_apps_details.delay(data)

        return Response({"message":"Google apps details added successfully"},status=status.HTTP_200_OK)