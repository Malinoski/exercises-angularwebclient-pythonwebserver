# exercises-angularwebclient-pythonwebserver

## Install using Docker 

### Web Client
```
git clone https://github.com/Malinoski/exercises-angularwebclient-pythonwebserver.git
cd exercises-angularwebclient-pythonwebserver/angularwebclient/
docker build -t iuri/angularwebclient .
docker images
docker run -p 49160:8080 -d iuri/angularwebclient
# Access http://YOU_HOST_IP:49160

```

### Web Server
TODO

