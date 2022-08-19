#!/usr/bin/python3
"""
enviar una solicitud y mostrar:
valor de X-request-id
"""
import urllib.request
import sys

url = sys.argv[1]
data_req = urllib.request.Request(url)

with urllib.request.urlopen(data_req) as response:
    content = response.headers.get("X-Request-Id")
    print(content)
