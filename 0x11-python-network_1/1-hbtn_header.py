#!/usr/bin/python3

"""
import required modules.
i.e : urllib.request
      sys
"""
import urllib.request
import sys

if __name__ == '__main__':
    """
    execute only if
    run as main
    """
    argv = sys.argv
    if len(argv) == 2:
        """
        if first argument is passed
        save it as url
        """
        url = argv[1]

        with urllib.request.urlopen(url) as response:
            headerDict = dict(response.headers)
        headerValue = headerDict.get('X-Request-Id')
        print(headerValue)
