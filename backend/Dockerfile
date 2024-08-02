# Base stage for production
FROM python:3.11.4-slim-bullseye AS prod

# Install Poetry
RUN pip install poetry==1.8.2

# Configure Poetry
RUN poetry config virtualenvs.create false
RUN poetry config cache-dir /tmp/poetry_cache

# Copy the project requirements
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Install the project dependencies
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main

# Copy the actual application code
COPY . /app/src/

# Reinstall dependencies if necessary
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["/usr/local/bin/python", "-m", "backend"]

# Development stage
FROM prod AS dev

# Install all dependencies (including dev)
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install
