#!/bin/bash -e
echo "----- Start -----"

# if [ -e $PWD/dist/*map ]; then
#     rm $PWD/dist/*.map
# fi

cp $PWD/db.json $PWD/dist/db.json

git pull --ff-only
git add .
git commit -m "$(date | md5 )"
git push origin master
echo "----- End -----"
