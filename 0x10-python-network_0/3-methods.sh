#!/bin/bash
# script that takes url, send a request and display Allowed methods curl s silent I header L location(redirection) -X method(OPTION) grep i case
curl -sILX OPTIONS "$1" | grep -i 'Allow:'| awk  -F ':' '{ print $2 }' | awk '{$1=$1;print}'
