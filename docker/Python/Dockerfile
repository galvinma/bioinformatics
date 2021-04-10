FROM ubuntu:18.04

# Apt
RUN apt-get update -y
RUN apt-get install -y --fix-missing \
        software-properties-common \
        build-essential \
        unzip \
        bzip2 \
        perl \
        nano \
        vim \
        wget \
        curl \
        make \
        automake

# Python
RUN apt-get install -y python3-pip python3-dev python3 \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*
COPY /requirements.txt /
RUN pip install -r /requirements.txt
