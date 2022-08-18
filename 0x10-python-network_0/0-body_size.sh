#!/bin/bash
#extraer el tamaño de mi encabezado en bytes
curl -sI "$1" | grep Content-Length | cut -f2 -d " "
