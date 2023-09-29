#!/usr/bin/python3

"""
import required modules.i.e : urllib.request, sys
"""
import urllib.request
import sys

if __name__ == '__main__':
    """
    execute only if run as main
    script that takes in a URL, sends a
    request to the URL and displays the value
    of the X-Request-Id variable found in
    the header of the response.
    """
    argv = sys.argv
    if len(argv) == 2:
        """
        if first argument is passed
        save it as url
        """
        url = argv[1]

        with urllib.request.urlopen(url) as response:
            headerValue = response.getheader('X-Request-Id')
        print(headerValue)
