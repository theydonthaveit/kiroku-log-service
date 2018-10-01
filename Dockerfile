# Use an official Python runtime as a parent image
FROM python:3.7-alpine
LABEL Author="Alan Williams"

# Set ENV for app
ENV APP_DIR /app

# Set the working directory to /app
WORKDIR /app

# Copy requirements to WORKDIR to install python dependencies
COPY ./app ${APP_DIR}

# Install any needed packages specified in requirements.txt
RUN apk update && \
    apk add supervisor && \
    pip install --trusted-host pypi.python.org -r requirements.txt && \
    mkdir -p /etc/supervisor && \
    mkdir -p web && \
    mkdir -p conf && \
    mkdir -p logs && \
    cat conf/*.ini >> /etc/supervisor/supervisord.conf

# Directories are created and can be populated
COPY ./app/logs ${APP_DIR}

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]