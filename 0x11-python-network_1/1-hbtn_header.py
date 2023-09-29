#!/usr/bin/python3

"""
import required modules.
i.e : urllib.request
      sys
"""
import sys
import urllib.request as request

if __name__ == '__main__':
    """
    execute only if run as main
    """
    argv = sys.argv
    if len(argv) == 2:
        """
        if first argument is passed save it as url
        """
        url = argv[1]

        with request.urlopen(url) as response:
            headerValue = response.getheader('X-Request-Id')
        print(headerValue)
