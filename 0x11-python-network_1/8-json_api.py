#!/usr/bin/python3
"""
Script que tome una letra a una url especifica
request a http://0.0.0.0:5000/search_user
con la letra como parametro
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data_req = requests.post(url, {"q", q})
    try:
        data_res = data_req.json()
        if data_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(data_res.get("id"), data_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
