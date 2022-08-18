#!/bin/bash
#do a post of variables with curl, muestra el cuerpo de la respuesta
curl -sX POST "$1" --data "email=test@gmail.com" --data "subject=I will always be here for PLD"
