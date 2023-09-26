#! /bin/sh

Y=$(date +%Y)
M=$(date +%m)
D=$(date +%d)
NEW_FOLDER_NAME="${Y}${M}${D}_$1"

cp -r template "$NEW_FOLDER_NAME"
cd "$NEW_FOLDER_NAME"

sed -i -e "s#TMP#${1}#g" template.py
mv template.py "${1}.py"
rm template.py-e
