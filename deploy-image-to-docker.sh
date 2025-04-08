#!/bin/sh

echo "$DOCKERHUB_TOKEN" | docker login -u $DOCKER_USERNAME --password-stdin

docker build -t $DOCKERHUB_USERNAME/dental:latest .

docker push $DOCKERHUB_USERNAME/dental:latest
