FROM python:3.9.12-slim

RUN pip install fastapi uvicorn poetry wheel virtualenv

WORKDIR /api

COPY ./app /api/app
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install

CMD ["python3", "-m", "uvicorn", "app.infrastructure.fastapi.main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]