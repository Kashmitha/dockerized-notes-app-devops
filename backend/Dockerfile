# Use python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code 
COPY app.py .

# Expose flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
