#!/usr/bin/python3
"""
obtener el header de la url y extrar el valor de [X-Request-Id]
"""
if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    data_req = requests.get(url)

    print(data_req.headers["X-Request-Id"])
