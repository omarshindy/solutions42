#!/bin/sh

set -xe

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Start the Django development server
echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000
