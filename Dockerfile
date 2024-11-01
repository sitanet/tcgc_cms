# Use your preferred Python version
FROM python:3.12.7

# Enable output buffering to see print statements immediately
ENV PYTHONUNBUFFERED=1

# Set the application port and working directory
ENV PORT=8080
WORKDIR /app

# Copy application code and install dependencies
COPY . /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the application port and set the startup command
EXPOSE 8080
CMD ["gunicorn", "follow_up_project.wsgi:application", "--bind", "0.0.0.0:8080"]
