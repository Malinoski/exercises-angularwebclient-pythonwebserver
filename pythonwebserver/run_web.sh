#!/usr/bin/env bash

cd rest/
python manage.py migrate

# Create superuser (https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Start server
python manage.py runserver 0.0.0.0:8000