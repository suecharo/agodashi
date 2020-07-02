FROM python:3.8.2-slim-buster

RUN apt update && \
    apt install -y --no-install-recommends \
    build-essential \
    curl \
    tini && \
    apt clean &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip setuptools wheel && \
    pip install -r requirements.txt

COPY . .

RUN python3 setup.py install

ENV AGODASHI_HOST 0.0.0.0
ENV AGODASHI_PORT 8080
ENV AGODASHI_DEBUG False

EXPOSE 8080

ENTRYPOINT ["tini", "--"]
CMD ["agodashi"]
