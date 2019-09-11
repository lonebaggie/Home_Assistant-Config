#!/bin/sh
username=$1
password=$2
extract=`curl -H "Content-Type: application/json" -X POST -d "{\"username\":\"$username\",\"password\":\"$password\"}" https://www.services.renault-ze.com/api/user/login`
echo $extract
token=`echo $extract|jq -r ".token"`
echo $token
