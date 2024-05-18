#!/bin/sh

docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

docker volume rm open-dental-site_static_volume
docker volume ls --format '{{.Name}}' | grep -E '^[a-f0-9]{64}$' | xargs -r docker volume rm

docker pull $DOCKERHUB_USERNAME/dental-nginx:latest
docker pull $DOCKERHUB_USERNAME/dental:latest
