# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

# Install system dependencies and inotify-tools for inotifywait
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN apt-get install curl -y

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod o+x /entrypoint.sh

EXPOSE 8000

ENV PORT 8000
# set hostname to localhost
ENV HOSTNAME "0.0.0.0"

ENTRYPOINT ["sh", "-c", " /entrypoint.sh"]
