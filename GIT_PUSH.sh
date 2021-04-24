#!/bin/bash -e

echo "----- Start -----"
find $PWD/dist | xargs rm -rf
# find $PWD/* -empty | xargs rm
git pull --ff-only
git add .
git commit -m "$(date | md5 )"
git push origin master
echo "----- End -----"
