# Use official Python image
FROM python:3.11-slim

# Set work directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
