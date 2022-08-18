#!/bin/bash
#send a POST wirh the content of a file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
