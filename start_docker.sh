#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 4000:4000 \
  --name=${app} \
  -v $PWD:/app ${app}