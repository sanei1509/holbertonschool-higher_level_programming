#!/bin/bash
#extraer ALLOWS
curl -sI "$1" | grep Allow | cut -f2- -d " "
