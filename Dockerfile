# syntax:docker/dockerfile:1
FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y git
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["flask", "run"]