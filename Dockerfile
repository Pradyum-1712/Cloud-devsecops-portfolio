# Use Alpine Linux for maximum security and smallest footprint
FROM python:3.12-alpine

# Create a non-privileged user to run the app (Security Best Practice)
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Install dependencies as the root user first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Change ownership to the non-privileged user
RUN chown -R appuser:appgroup /app

# Switch to the non-privileged user
USER appuser

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
