#!/bin/bash
# script that takes url, send a request Method Delete and display the body curl s silent  L location(redirection) X for method (GET,POST...)
curl -sL -X DELETE "$1"
