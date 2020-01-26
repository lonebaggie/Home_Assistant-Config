m1='http://192.168.1.91/web/message?text='
m2=$(cat)
m3='&type=1&timeout=10'
m2=${m2// /%20}
curl --silent --output /dev/null $m1$m2$m3