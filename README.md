### Step1: Create virtual environment using below command
    $ python -m venv environment_name
    
### Step2: Activate virtual environment
    $ source environment_name/bin/activate

### Step3: Install requirements of project using below command
    $ pip install -r requirements.txt

### Step4: Apply makemigrations and migrate using below commands
    $ python manage.py makemigrations
    $ python manage.py migrate
    
### Step5: Start django server using below command
    $ python manage.py runserver
    
### Step6: Check redis server is running or not
    $ sudo service redis-server status
    $ sudo service redis-server start - <span style="color: red">Redis server start using this command</span>
    
### Step7: Start celery server in new terminal using below command
    $ celery -A google_play_scraper_project worker --beat -l info

** In this project we have two APIs first one is GET and second is POST. **

### URL of the API: http://localhost:8000/google_apps_store_details/

1. POST API: This API is used to scrap data from the given "Google Apps Store" URL and store the app details in the particular table using celery.
   request object = {
    "url":"https://play.google.com/store/games?hl=en&gl=US",
    "lang":"en",
    "country":"us"
   }
   ![image](https://github.com/pminesh/lahagora_test_task/assets/43671273/18959663-dae8-480e-b286-89552c8c9238)


2. GET API: This API is used to get all data of apps from the database.
   ![image](https://github.com/pminesh/lahagora_test_task/assets/43671273/c05ad597-aa6d-4822-96a7-96359c416932)

