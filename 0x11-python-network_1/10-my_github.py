#!/usr/bin/python3
"""
    tomar tus credenciales de GitHub credential (username and password)
    usar la api para mostrar el id
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    data_res = requests.get(url, auth=(user, passwd))

    data_json = data_res.json()
    print(data_json["id"])
