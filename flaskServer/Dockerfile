# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

RUN mkdir /data

# Run the app
CMD ["python", "app.py"]

# Run Python in unbuffered mode so logs show immediately
ENV PYTHONUNBUFFERED=1
