#!/bin/sh
python manage.py migrate --noinput
gunicorn redirekter.wsgi --workers 2 --bind "0.0.0.0:$PORT"
