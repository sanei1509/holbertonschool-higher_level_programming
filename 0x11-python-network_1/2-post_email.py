#!/usr/bin/python3
"""

"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({"email": email})


data = data.encode()

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode())
