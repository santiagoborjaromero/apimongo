FROM python:3.12.7-slim-bullseye

COPY . /apimongo
WORKDIR /apimongo

RUN pip install -r packages.txt

ENTRYPOINT uvicorn main:app --port 5000 --reload   
