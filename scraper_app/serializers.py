from rest_framework import serializers
from scraper_app.models import AppDetails, Developer

class DeveloperSerializer(serializers.ModelSerializer):
    """
    Serializer for the Developer model.
    """
    class Meta:
        model = Developer
        fields = ['developer', 'developerId', 'developerEmail', 'developerWebsite', 'developerAddress']

class AppDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for the AppDetails model.
    """
    developer_details = serializers.SerializerMethodField()

    class Meta:
        model = AppDetails
        fields = ['id', 'title', 'description', 'score',
                  'ratings', 'reviews', 'appId', 'url', 'categories', 'developer_details']

    def get_developer_details(self, obj):
        """
        Method to retrieve and serialize the related Developer details.
        """
        try:
            developer_details = Developer.objects.filter(app_details_id=obj.id).first()
            serializer = DeveloperSerializer(developer_details)
            return serializer.data
        except Developer.DoesNotExist:
            return None
