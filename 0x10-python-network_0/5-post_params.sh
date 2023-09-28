#!/bin/bash
# script that takes a url display body send post with variables curl s silent -X method (POST) -d data to pass using POST in body
curl -s -X POST -d "email:test@gmail.com" -d "subject:I will always be here for PLD" "$1"
