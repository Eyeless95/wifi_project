#!/usr/bin/env bash

NAME="wifi_project"
DJANGODIR=/opt/wifi_service/wifi_project
SOCKFILE=localhost:8000
USER=root
GROUP=root
NUM_WORKERS=2
DJANGO_SETTINGS_MODULE=wifi.settings
DJANGO_WSGI_MODULE=wifi.wsgi


echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../wifi_env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../wifi_env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=$SOCKFILE \
  --log-level=debug \
  --log-file=/var/log/supervisor/wifi_supervisor_log.log
