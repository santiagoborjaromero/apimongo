FROM python:3.12.7-slim-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        gcc \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . .

RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000-5005
# CMD ["uvicorn","main:app","--host 0.0.0.0","--port 5001"]

