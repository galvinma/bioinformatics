#!/bin/sh

# Builds a local docker image 
# Accepts image name and tage as a positional argument
# ./docker-entrypoint.sh NAME:TAG

docker build . -t $1
