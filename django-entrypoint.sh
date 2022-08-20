#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py grpcrunserver 0.0.0.0:50051 & python manage.py runserver 0.0.0.0:8000
exec "$@"