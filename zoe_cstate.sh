#!/bin/sh
if [ "$1" = "now" ]; then 
  DOW=$(date +"%a")
  d=$(echo "$DOW" | tr '[:upper:]' '[:lower:]')
else
  d=$1
fi
cat ./schedule.txt |jq  --arg v $d '.schedule|to_entries[]|{day: .key, start: .value.start, duration: .value.duration}| select(.day == $v)'