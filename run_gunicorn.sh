#!/bin/bash
set -e

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn -b 0.0.0.0:8000 -w 3 \
    --access-logfile=- \
    --log-file=- \
    --access-logformat='%(h)s "%(r)s" %(s)s %(b)s "%(f)s"' \
    biketour.wsgi
