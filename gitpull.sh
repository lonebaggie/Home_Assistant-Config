#!/bin/bash

ha core check

git add .
git status
echo -n "Updated config: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git pull origin master

exit
