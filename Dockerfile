# Pull a base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a working directory for the django project
WORKDIR /code

# Copy requirements to the container
COPY ./Pipfile ./Pipfile.lock /code/

# Install the requirements to the container
RUN pip install pipenv
RUN pipenv install --system --deploy

# Copy the backend project files into the working directory
ADD . /code/

# Open a port on the container
EXPOSE 8000
