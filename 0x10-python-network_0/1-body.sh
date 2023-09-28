#!/bin/bash
# script that takes url, send a request and display the body curl s silent  L location(redirection)
curl -sL -X GET "$1"
