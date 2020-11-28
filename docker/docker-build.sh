docker build . -t umi-validation

#!/bin/sh

# Builds a local docker image 
# Accepts image name as a positional argument
# ./docker-entrypoint.sh IMAGENAME

docker build . -t $1