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

Access http://localhost:8001/admin

* Deploy the web client

```
cd ..
cd angularwebclient/
docker-compose up -d
```

Access http://localhost:8002

