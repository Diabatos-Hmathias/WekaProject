# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir Flask

# Expose the port on which your Flask app runs
EXPOSE 5000

# Define the command to run your Flask app when the container starts
CMD ["python", "weka.py"]
