FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src
COPY ./alembic.ini /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["python", "src/main.py"]