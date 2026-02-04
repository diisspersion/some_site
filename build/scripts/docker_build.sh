#!/bin/bash

IMAGE_NAME="basic_app"
CONTAINER_NAME="basic_app"
DOCKERFILE_PATH="./build/Dockerfile"

if ! sudo -v; then
  echo "Error: sudo authentication failed. Aborting."
  exit 1
fi

echo "--- Building/updating the image ---"
sudo docker build -f "$DOCKERFILE_PATH" -t "$IMAGE_NAME" .

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
