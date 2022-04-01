#!/bin/sh

set -o errexit

#timeout 60 sh -c "until nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do sleep 1; done"

python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput

exec gunicorn home_interview.wsgi:application --preload --workers=3 -b 0.0.0.0:8000
