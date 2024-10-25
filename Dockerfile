# pull official base image (try a different version if the issue persists)
FROM python:3.11-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies (optional if additional packages are required)
# RUN apt-get update && apt-get install -y libpq-dev gcc

# Install system dependencies for running PostgreSQL and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project files to the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# specify the command to run your app (change if you're not using Django's default dev server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
