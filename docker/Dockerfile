# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set the working directory inside the container
WORKDIR /app

# Install Python and pip (since Ubuntu does not come with Python pre-installed)
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copy the application files from your local system to the /app directory inside the container
COPY ../app /app

# Install Python dependencies (Flask)
RUN pip3 install Flask

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]

