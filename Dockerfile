# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Faster, cleaner Python
ENV PYTHONDONTWRITEBYTECODE=1         PYTHONUNBUFFERED=1

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app ./app

EXPOSE 5000

# Run the app
CMD ["python", "app/app.py"]
