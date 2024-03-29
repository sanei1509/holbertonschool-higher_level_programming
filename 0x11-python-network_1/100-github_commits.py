#!/usr/bin/python3
"""
traer 10 commits de github usando su api
"""
if __name__ == "__main__":
    import requests
    import sys

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    data = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(arg2, arg1))

    json_commits = data.json()

    cont = 0
    for commit in json_commits:
        if cont < 10:
            print(commit["sha"], end=": ")
            print(commit["commit"]["author"]["name"])
        cont += 1
