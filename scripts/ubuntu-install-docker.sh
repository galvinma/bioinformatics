#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y build-essential \
        software-properties-common \
        zlib1g-dev
        libbz2-dev \
        liblzma-dev \
        tabix \
        curl \
        unzip \
        make \
        bzip2 \
        nano \
        vim \
        gcc \
        g++ \
        git \
        apt-transport-https \
        ca-certificates \
        gnupg-agent \
    && apt-get clean \
    && apt-get purge

# Docker
sudo apt install docker.io
sudo groupadd docker
sudo usermod -aG docker ubuntu
sudo systemctl enable docker

# Post
sudo usermod -aG docker ${USER}

# Log in and out