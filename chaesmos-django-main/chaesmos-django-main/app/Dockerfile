FROM python:3.9-alpine

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . .
