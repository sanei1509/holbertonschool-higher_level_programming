#!/usr/bin/python3
"""
scrip que haga un fetch manejando los errores (try, except)
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://intranet.hbtn.io/status"

    data_req = requests.get(url)
    if data_req.status_code >= 400:
        print("Error code: {}".format(data_req.status_code))
    else:
        print(data_req.text)
