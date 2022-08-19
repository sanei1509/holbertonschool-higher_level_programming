#!/usr/bin/python3
"""
enviar un mail a la url pasada y mostrar el cuerpo de la respuesta
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})

    data = data.encode()
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode())
