FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}

# Command to run the application
CMD ["python", "agent.py"]
