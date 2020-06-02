#!/bin/bash

## chmod +x some.sh

echo "-------Auto Git Begin-------"
git pull
git add .
now="$(date +"%Y-%m-%d-%H-%M-%S")"
git commit -m "${now}"
echo "****************** commit is:$1 ${now} ***********"
git push origin master
echo "--------End--------"
