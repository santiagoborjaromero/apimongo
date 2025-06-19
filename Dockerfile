FROM python:3.12.7-slim-bullseye

COPY . /apimongo
WORKDIR /apimongo

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 5000
