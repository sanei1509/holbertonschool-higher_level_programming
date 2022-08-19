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
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    data_req = requests.post(url, {"q": q})
    try:
        data_json = data_req.json()
        if len(data_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data_json["id"], data_json["name"]))
    except ValueError:
        print("Not a valid JSON")
