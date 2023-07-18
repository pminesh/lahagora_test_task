from google_play_scraper_project.celery import celery_app
from google_play_scraper import app
from bs4 import BeautifulSoup
from scraper_app.models import AppDetails, Developer
import json
import re
import requests

@celery_app.task
def store_google_play_apps_details(data):
    url=data["url"]
    lang=data["lang"]
    country=data["country"]

    """Step1: Scrape the data from given url like https://play.google.com/store/games?hl=en&gl=US"""
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object from the response content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all the <a> tags with the "href" attribute containing "details?id="
            app_links = soup.find_all("a", href=re.compile(r"\/store\/apps\/details\?id=.*"))
            
            """Step2: Filter out the package names from the scraped data [Eg: package name looks like com.snakeattack.game]"""
            # Extract the app IDs from the URLs
            app_ids = [link["href"].split("=")[1] for link in app_links]
            
            all_app_ids = list(set(app_ids))

            """Step3: Once you have all the package names fetch the package details from playstore. 
            (To fetchpackage details you can use this library https://pypi.org/project/google-play-scraper/ ) """
            # Print the app IDs
            for app_id in all_app_ids:
                result = app(
                    app_id,
                    lang=lang,
                    country=country
                )
                app_details = json.loads(json.dumps(result))

                appId_is_exist = AppDetails.objects.filter(appId=app_id).exists()

                """Step4: store all these data in database"""
                if appId_is_exist is False:
                    app_data = AppDetails(
                    title = app_details['title'],
                    description = app_details['description'],
                    score = int(app_details['score']) if app_details['score'] is not None else 0,
                    ratings = int(app_details['ratings']) if app_details['ratings'] is not None else 0,
                    reviews = int(app_details['reviews']) if app_details['reviews'] is not None else 0,
                    appId = app_details['appId'],
                    url = app_details['url'],
                    categories = app_details['categories'])
                    app_data.save()

                    developer_data = Developer(
                        developer = app_details['developer'],
                        developerId = app_details['developerId'],
                        developerEmail = app_details['developerEmail'],
                        developerWebsite = app_details['developerWebsite'],
                        developerAddress = app_details['developerAddress'],
                        app_details = app_data
                    )

                    developer_data.save()
        else:
            print("Error:", response.status_code)
    except Exception as error:
        print("Error:", error)