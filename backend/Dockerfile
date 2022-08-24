FROM python:3.9.0-slim-buster

# 파이썬 .pyc 파일을 생성하지 못하도록 설정
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하는 설정
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python - --version 1.1.13 \
    && apt-get install -y iputils-ping

# poetry 설치를 위한 PATH 설정
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /api

COPY pyproject.toml poetry.lock ./

# 패키지 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# app폴더를 컨테이너 api/app폴더안에 복사
COPY ./app /api/app

CMD ["uvicorn", "app.infrastructure.fastapi.main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
