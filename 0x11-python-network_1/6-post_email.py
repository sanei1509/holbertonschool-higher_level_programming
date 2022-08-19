#!/usr/bin/python3
"""
hacer un post del email pasado a la url, mostrar el cuerpo
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data_req = requests.post(url, {"email": email})

    print(data_req.text)
