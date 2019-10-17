 #!/bin/sh
extract=`curl -H "Content-Type: application/json" -X POST -d "{\"username\":\"$1\",\"password\":\"$2\"}" https://www.services.renault-ze.com/api/user/login`
token=`echo $extract|jq -r ".token"`
vin=`echo $extract|jq -r ".user.vehicle_details.VIN"`
#charge= `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" https://www.services.renault-ze.com/api/vehicle/$vin/charge`
battery=`curl -H  "Authorization: Bearer $token" https://www.services.renault-ze.com/api/vehicle/$vin/battery`
cstate=`curl -H  "Authorization: Bearer $token" https://www.services.renault-ze.com/api/vehicle/$vin/charge/scheduler/onboard`
echo $cstate| jq "."   > schedule.txt
echo $battery|jq .

