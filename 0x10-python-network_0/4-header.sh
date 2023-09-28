#!/bin/bash
# takes url send GET with some value display Body curl -s silent -X method(GET) -H set custom header when using GET
curl -s -X GET -H "X-School-User-Id: 98" "$1"
