FROM ubuntu:18.04

# ENV
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Apt
RUN apt-get update -y 
RUN apt-get install -y --fix-missing \
        software-properties-common \
        build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        libbz2-dev \
        liblzma-dev \
        unzip \
        bzip2 \
        perl \
        nano \
        vim \
        wget \
        curl \
        make \
        automake \
        gcc \
        gfortran \
        fort77 \
        xorg-dev \
        libblas-dev \
        gcc-multilib \
        gobjc++ \
        aptitude \
        libpcre2-dev \
        libcurl4 \
        libcurl4-openssl-dev \
        default-jre \
        default-jdk \
        openjdk-8-jdk \
        openjdk-8-jre 

# R
RUN wget https://cran.r-project.org/src/base/R-4/R-4.0.4.tar.gz \
  && tar -xzf R-4.0.4.tar.gz \
  && cd R-4.0.4 \
  && CPPFLAGS=-I$HOME/include LDFLAGS="-L$HOME/lib -Wl,-rpath=$HOME/lib" ./configure --prefix=$HOME --with-cairo --with-blas --with-lapack --enable-R-shlib --with-pcre1 --with-readline=no --with-x=no \
  && make
ENV PATH=${PATH}:/R-4.0.4/bin