#!/bin/sh
python manage.py migrate --noinput

# python manage.py collectstatic --noinput
# python manage.py runserver "$VCAP_APP_HOST:$VCAP_APP_PORT"

gunicorn rtpp--workers 2 --bind "0.0.0.0:$PORT"
