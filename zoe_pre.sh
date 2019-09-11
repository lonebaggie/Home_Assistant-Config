#!/bin/sh
extract=`curl -H "Content-Type: application/json" -X POST -d "{\"username\":\"$1\",\"password\":\"$2\"}" https://www.services.renault-ze.com/api/user/login`
token=`echo $extract|jq -r ".token"`
vin=`echo $extract|jq -r ".user.vehicle_details.VIN"`
echo `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" https://www.services.renault-ze.com/api/vehicle/$vin/air-conditioning`
