#!/usr/bin/python3
"""
manejar el try except de los errores
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import URLError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            content.decode()
    except URLError as err:
        print("Error code: ", err.code)
