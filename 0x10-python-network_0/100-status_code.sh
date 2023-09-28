#!/bin/bash
# script that takes url as argument ad return status
curl -s -o /dev/null -w "%{http_code}" "$1"
