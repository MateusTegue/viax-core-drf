FROM python:3.12

# innstall SSH client
RUN apt-get update && apt-get install -y openssh-client

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the application to the working directory
COPY . /app

# start the SSH tunnel
CMD python manage.py runserver 0.0.0:8000