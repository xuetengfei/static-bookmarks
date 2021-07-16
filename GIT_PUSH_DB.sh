#!/bin/bash -e

echo "----- Start -----"

rm $PWD/dist/*.map
cp $PWD/db.json $PWD/dist/db.json
# find $PWD/* -empty | xargs rm
git pull --ff-only
git add .
git commit -m "$(date | md5 )"
git push origin master
echo "----- End -----"
