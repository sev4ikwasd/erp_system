# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /erp_system
COPY . .
RUN pip install -r ./requirements.txt
RUN chmod +x ./django-entrypoint.sh