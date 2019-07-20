FROM python:3.6

# Environment Variables
ENV PYTHONUNBUFFERED 1

# Run Commands

# # Place to keep the project code
RUN mkdir /webapps

# # Tell docker where to run the next commands
WORKDIR /webapps

# # Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
RUN pip install -U pip setuptools

# # Install python requirements
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
ADD . /webapps/

# Django service
EXPOSE 8000