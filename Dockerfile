# pull official base image (try a different version if the issue persists)
FROM python:3.11-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies (optional if additional packages are required)
# RUN apt-get update && apt-get install -y libpq-dev gcc

# upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project files to the container
COPY . .

# specify the command to run your app (change if you're not using Django's default dev server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
