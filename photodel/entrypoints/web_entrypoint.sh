#!/bin/sh

#python manage.py migrate --fake
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000

exec "$@"
