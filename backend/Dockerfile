FROM python:3

RUN pip install poetry==1.8.2

RUN poetry config virtualenvs.create false

WORKDIR /app/src

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
