#!/usr/bin/python3
"""script para obtener -> https://intranet.hbtn.io/status
    - only with urllib
"""
if __name__ == "__main__":
    import urllib.request

    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: ", type(content))
        print("\t- content: ", content)
        print("\t- utf8 content: ", content.decode())
