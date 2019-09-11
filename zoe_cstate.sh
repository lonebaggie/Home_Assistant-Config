 #!/bin/sh
cat ./schedule.txt |jq --arg v $1 '.schedule[$v]'