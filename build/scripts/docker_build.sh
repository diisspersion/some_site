#!/bin/bash

IMAGE_NAME="basic_app"
CONTAINER_NAME="basic_app"
DOCKERFILE_PATH="./build/Dockerfile"

RED='\033[0;31m'
NC='\033[0m' # No Color


if ! sudo -v; then
  echo -e "${RED}Error: sudo authentication failed. Aborting."
  exit 1
fi

echo "--- Building/updating the image ---"
if ! sudo docker build -f "$DOCKERFILE_PATH" -t "$IMAGE_NAME" .; then
  echo -e "${RED}Error: Building/updating the image."
  exit 1
fi

echo "--- Stopping and removing the old container (if it exists) ---"
sudo docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

echo "--- Starting a new container ---"
sudo docker run -d \
  -p 8000:8000 \
  --name "$CONTAINER_NAME" \
  "$IMAGE_NAME"

echo "--- Cleaning up old (dangling) images ---"
sudo docker image prune -f

echo "Container $CONTAINER_NAME has been started."

read
