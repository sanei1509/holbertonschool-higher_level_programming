#!/bin/bash
# mostrar en la respuesta el status de la respuesta de la peticion
curl -s -o /dev/null -w "%{http_code}" "$1"
