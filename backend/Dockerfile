# Base stage for production
FROM python:3.11.4-slim-bullseye AS prod

# Install system dependencies
RUN apt-get update && apt-get install -y curl && apt-get clean

# Install Poetry
RUN pip install poetry==1.8.2

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false

# Set the working directory
WORKDIR /app/src

# Copy only the project requirement files to install dependencies
COPY pyproject.toml poetry.lock ./

# Install the project dependencies
RUN poetry install --only main

# Copy the actual application code
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["/usr/local/bin/python", "-m", "backend"]

# Development stage
FROM prod AS dev

# Install all dependencies (including dev)
RUN poetry install
