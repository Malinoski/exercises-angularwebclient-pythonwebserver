# exercises-angularwebclient-pythonwebserver

## Install using Docker 

### Pull the code
git clone https://github.com/Malinoski/exercises-angularwebclient-pythonwebserver.git
cd exercises-angularwebclient-pythonwebserver

### Web Client
```
cd angularwebclient/
docker build -t iuri/angularwebclient .
docker images
docker run -p 49160:8080 -d iuri/angularwebclient
cd ..
# Access http://localhost:49160

```

### Web Server
```
cd pythonwebserver/
chmod +x run_web.sh
docker-compose up
# Access http://localhost:8001/admin
```
