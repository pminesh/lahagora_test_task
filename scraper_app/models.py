from django.db import models

class AppDetails(models.Model):
    """
    Model representing the details of an app.
    """
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    score = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    appId = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    categories = models.JSONField(default=list)

    def __str__(self):
        """
        Returns a string representation of the AppDetails object.
        
        :return: The title of the app.
        :rtype: str
        """
        return self.title
    
    class Meta:
        """
        Meta options for the AppDetails model.
        """
        db_table = 'app_details_tb'
    
class Developer(models.Model):
    """
    Model representing the developer details.
    """
    developer = models.CharField(max_length=250, null=True, blank=True)
    developerId = models.CharField(max_length=250, null=True, blank=True)
    developerEmail = models.CharField(max_length=150, null=True, blank=True)
    developerWebsite = models.CharField(max_length=50, null=True, blank=True)
    developerAddress = models.CharField(max_length=250, null=True, blank=True)
    app_details = models.ForeignKey(AppDetails, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        Returns a string representation of the Developer object.
        
        :return: The name of the developer.
        :rtype: str
        """
        return self.developer
    
    class Meta:
        """
        Meta options for the Developer model.
        """
        db_table = 'developer_tb'