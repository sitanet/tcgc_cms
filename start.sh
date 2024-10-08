#!/bin/bash

# Activate the virtual environment (if using one)
# Uncomment the following line if you have a virtual environment setup
# source venv/bin/activate

echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting the Django development server..."
python manage.py runserver 0.0.0.0:8000

# Optionally, you could add more steps like checking the environment variables or cleaning up files if needed.
