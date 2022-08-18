#!/bin/bash
#pass a variable in the header of the request
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
