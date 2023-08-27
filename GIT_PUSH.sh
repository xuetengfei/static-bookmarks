#!/bin/bash -e

echo "----- Start -----"

if [ -d $PWD/dist ]; then
    find $PWD/dist | xargs rm -rf
fi


if [ -e $PWD/tempCodeRunnerFile.py ]; then
    rm $PWD/tempCodeRunnerFile.py
fi


npm run build
# npx parcel build index.html

cp ./db.json ./dist/db.json
# find $PWD/* -empty | xargs rm
git pull --ff-only
git add .
git commit -m "$(date | md5 )"
git push origin master
echo "----- End -----"
