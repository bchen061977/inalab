# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Setting default value here. Also there's a default value in the app.py. To change modify docker-compose environment var
ENV CONTENT='Hello, World!'

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application 
COPY . .

# Expose port 5000 
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

