# Python web service

* Install Python 3 and PyCharm CE 

* Create the PyCharm web sever project, using a new environment with Python 3 interpreter (i.e.: /usr/local/Cellar/python/3.7.4/bin/python3)

* Open the PyCharm Terminal and install the dependences:

```
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pygments
```

* Create the project, app, etc..
```
mkdir [PYCHARM_WEBSERVER_PROJECT_NAME]
cd [PYCHARM_WEBSERVER_PROJECT_NAME]

# Install some stuffs
django-admin startproject [PROJECT_NAME]
python manage.py startapp [MY_APP]

# Create some code (models, views, urls, etc..)
# ....

# Do not forget to sync models with database for the first time, ex.: 
python manage.py makemigrations polls 
python manage.py makemigrations snippets 
python manage.py migrate
```

* Tests libs (it will create and destroy a new db for the tests)
    
```
cd [PROJECT_NAME]
python manage.py test 
```
    
* Test on python web client (this will simulate a web client. This will NOT create a db like before)
    
```
# Go to project python console
cd [PROJECT_NAME]
python manage.py shell

# Prepare and run tests
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
response = client.get('/') # The call is http://localhost:8001/
response.status_code # 200
response.content # b'The web service works!' 
from django.urls import reverse
response = client.get(reverse('polls:index')) 
response.content # html elements
response.context['latest_question_list'] # html elements
```

* Test on terminal

```
# curl (get the token and use the token)
curl -d "username=admin&password=admin" -X POST http://127.0.0.1:8001/core/api-token-auth/
curl http://127.0.0.1:8001/core/hello -H 'Authorization: Token $TOKEN'

# httpi (get the token and use the token)
http post http://127.0.0.1:8001/core/api-token-auth/ username=admin password=admin
http http://127.0.0.1:8001/core/hello 'Authorization: Token $TOKEN'
```

* Run the server
```
cd [PROJECT_NAME]
python manage.py runserver 8001
```
