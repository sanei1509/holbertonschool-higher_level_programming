#!/usr/bin/python3
"""script para obtener -> https://intranet.hbtn.io/status
    - only with urllib
"""
import urllib.request

url = "https://intranet.hbtn.io/status"
data_req = urllib.request.Request(url)

with urllib.request.urlopen(data_req) as response:
    content = response.read()
    tipo = response.code
    print("Body response:")
    print("\t- type: ", type(content))
    print("\t- content: ", content)
    print("\t- utf8 content: ", content.decode())
