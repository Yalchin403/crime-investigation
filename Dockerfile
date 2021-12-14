FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED 11
COPY ./reqs.txt /reqs.txt
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install python3-dev default-libmysqlclient-dev build-essential libssl-dev
RUN pip install -r /reqs.txt
COPY . /app
WORKDIR /app