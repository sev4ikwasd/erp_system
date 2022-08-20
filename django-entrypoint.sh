#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py run_grpc_server 0.0.0.0:55000 & python manage.py runserver 0.0.0.0:8000 & python manage.py consume_parse_queue
exec "$@"