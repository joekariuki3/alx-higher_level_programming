#!/usr/bin/python3

"""
import required modules: request, sys
"""
import requests
import sys

if __name__ == '__main__':
    """
    execute only if run as main
    script that takes url returns value of
    a parameter in the header
    """
    argv = sys.argv
    if len(argv) == 2:
        """
        if first argument is passed det it as the url
        """
    url = argv[1]
    res = requests.get(url)
    headerValue = res.headers.get('X-Request-Id')
    print(headerValue)
