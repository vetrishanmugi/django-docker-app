# Django Docker App

This is a sample Django project running in Docker.

## How to run

1. Build the image:
   docker build -t django-docker-app .

2. Run the container:
   docker run -p 8000:8000 django-docker-app

Then open http://localhost:8000/hello/

## Project Structure

- manage.py
- hello/        # Django app
- myproject/    # Django project settings
- Dockerfile
- requirements.txt

