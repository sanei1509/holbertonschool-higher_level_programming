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
                        .format(arg1, arg2))

    json_commits = data.json()

    # cont = 0
    for commit in json_commits[:10]:
        # if cont < 10:
        print(commit["sha"], end=": ")
            # print(commit["commit"]["author"]["name"])
        print(commit.get('commit').get('author').get('name'))
        # cont += 1
