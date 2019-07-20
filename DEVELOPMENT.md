# Python web service

* Install Python 3 and PyCharm CE 

* Create the PyCharm web sever project, using a new environment with Python 3 interpreter (i.e.: /usr/local/Cellar/python/3.7.4/bin/python3)

* Open the PyCharm Terminal and install the dependences:

```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

* Create the project, app, etc..
```
mkdir [PYCHARM_WEBSERVER_PROJECT_NAME]
cd [PYCHARM_WEBSERVER_PROJECT_NAME]
django-admin startproject [PROJECT_NAME]
python manage.py startapp [MY_APP]
...
```

* Run the server
```
cd [PROJECT_NAME]
python manage.py runserver 8001
```

# Angular web client

* Open the terminal and create the project
```
mkdir [ECLIPSE_WEBCLIENT_PROJECT_NAME]
cd [ECLIPSE_WEBCLIENT_PROJECT_NAME]
git clone --depth=1 https://github.com/angular/angular-seed.git angularwebclient
npm install
```

* Open Eclipse and create a simple project with the previous code

* Run the web client
```
cd [ECLIPSE_WEBCLIENT_PROJECT_NAME]
node app.js
```