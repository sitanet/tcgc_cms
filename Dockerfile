# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Run the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "follow_up_project.wsgi:application"]
