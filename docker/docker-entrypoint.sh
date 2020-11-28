#!/bin/sh

# Note this script depends on an .env file with a defined APPLICATION_MODE
# Accepts a container name as a positional argument
# ./docker-entrypoint.sh IMAGENAME

export $(grep -v '^#' .env | xargs)

if [ ${APPLICATION_MODE} == 'production' ]
then
    echo "In production mode..."
    docker run -v $PWD/host/dir:/container/dir -it $1 bash
else
    echo "In test/dev mode..."
fi