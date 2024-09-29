# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python app from the parent directory of docker/ (db_service.py)
COPY ../../dbservice/db_service.py /app/

# Optionally copy the requirements.txt if it exists and install dependencies
# COPY ../requirements.txt /app/
# RUN pip install -r requirements.txt

# Install Flask and SQLAlchemy
RUN pip install Flask Flask-SQLAlchemy

# Expose port 5001
EXPOSE 5001

# Command to run the Flask app
CMD ["python", "db_service.py"]

