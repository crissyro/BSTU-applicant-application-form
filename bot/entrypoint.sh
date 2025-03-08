#!/bin/bash

echo "Waiting for MongoDB to start..."
until mongosh --host mongodb --eval "print(\"MongoDB is ready\")" 2>/dev/null
do
  sleep 1
done

echo "Starting bot..."
exec python3 app/main.py
