#!/usr/bin/python3

"""
get required modules requests, sys
"""
import requests
import sys

if __name__ == '__main__':
    """
    execute only when run as main
    Arguments : Gitub repository_name and ownername uses Github API
    Return 10 latest commits
    """
    argv = sys.argv
    if len(argv) == 3:
        """
        first argument repoName
        second argument username
        """
        repoName = argv[1]
        username = argv[2]

        url = f"https://api.github.com/repos/{username}/{repoName}/commits"
        values = {'per_page': 10}
        resp = requests.get(url, params=values)
        Alldata = resp.json()

        for data in Alldata:
            sha = data.get('sha')
            commit = data.get('commit')
            author = commit.get('author')
            authorName = author.get('name')
            print(f"{sha}: {authorName}")
