#!/bin/bash
# Build docker image for linux system (lightsail)
docker buildx build --platform=linux/amd64 -t  app-container .
# Push container to AWS
aws lightsail push-container-image --region us-east-1 --service-name content-api --label app-container --image app-container:latest

# Use the below command to deploy container, but MAKE SURE to update the image in containers.json
# aws lightsail create-container-service-deployment --service-name content-api --containers file://util/aws/containers.json --public-endpoint file://util/aws/public-endpoint.json