#!/bin/bash
#do a post of variables with curl
curl "$1" --data "email=test@gmail.com" --data "subject=I will always be here for PLD"
