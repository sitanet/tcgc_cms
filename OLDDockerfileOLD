# Use the preferred Python version
FROM --platform=linux/amd64 python:3.11-bookworm

# Enable output buffering to see print statements immediately
ENV PYTHONUNBUFFERED=1

# Set the application port and working directory
WORKDIR /tcgc_cms

# Copy application dependencies file to container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the application port and set the startup command
EXPOSE 8000
CMD ["gunicorn", "follow_up_project.wsgi:application", "--bind", "0.0.0.0:8000"]
