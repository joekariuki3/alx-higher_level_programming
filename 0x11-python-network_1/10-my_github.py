#!/usr/bin/python3

"""
get required modules requests, sys
"""
import requests
import sys

if __name__ == '__main__':
    """
    execute only when run as main
    Arguments : Gitub username and psw uses Github API
    Return User ID
    """
    argv = sys.argv
    if len(argv) == 3:
        """
        first argument username
        second argument pswd
        """
        username = argv[1]
        password = argv[2]

        values = {'username': username, 'password': password}
        url = "https://api.github.com/user"
        resp = requests.get(url, auth=(username, password))
        userData = resp.json()
        userId = userData.get('id')
        print(userId)
