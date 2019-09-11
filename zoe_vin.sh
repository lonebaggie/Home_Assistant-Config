#!/bin/sh
username=$1
password=$2
extract=`curl -H "Content-Type: application/json" -X POST -d "{\"username\":\"$username\",\"password\":\"$password\"}" https://www.services.renault-ze.com/api/user/login`
vin=`echo $extract|jq -r ".user.vehicle_details.VIN"`
echo $vin
