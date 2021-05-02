#!/bin/bash -e

echo "----- Start -----"

if [ -d $PWD/dist ]; then
    find $PWD/dist | xargs rm -rf
fi

# npx parcel build index.html
npx parcel build index.html

# find $PWD/* -empty | xargs rm
git pull --ff-only
git add .
git commit -m "$(date | md5 )"
git push origin master
echo "----- End -----"
