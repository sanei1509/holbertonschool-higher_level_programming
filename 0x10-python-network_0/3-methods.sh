#!/bin/bash
# extraer todos los metodos http que soporta
curl -sI "$1" | grep Allow | cut -f2- -d " "
