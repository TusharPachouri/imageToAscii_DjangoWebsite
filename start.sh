#!/bin/bash

# Path to your Django project's WSGI file
WSGI_MODULE="imageToAscii.wsgi"

# Run Gunicorn
exec gunicorn ${WSGI_MODULE}:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --log-file=-
