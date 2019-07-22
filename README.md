# Install using Docker 

* Get the code
```
git clone https://github.com/Malinoski/exercises-angularwebclient-pythonwebserver.git
cd exercises-angularwebclient-pythonwebserver
```

* Deploy the web server
```
cd pythonwebserver/
docker-compose up -d 
```

http://localhost:8001/admin (user: admin, pass:admin)

http://localhost:8001/polls/app/ (internal app)

http://localhost:8001/polls/questions/?format=json (json)

* Deploy the web client

```
cd ..
cd angularwebclient/
docker-compose up -d
```

http://localhost:8002

