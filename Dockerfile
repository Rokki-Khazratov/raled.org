FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install --no-cache-dir poetry && \
    poetry install --no-dev


RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

ENV DB_NAME $DB_NAME
ENV DB_USER $DB_USER
ENV DB_PASSWORD $DB_PASSWORD
