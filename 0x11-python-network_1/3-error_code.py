#!/usr/bin/python3

"""
import required modules.
i.e : urllib.request
      urllib.error
      sys
"""
import sys
import urllib.request as request
import urllib.error as error

argv = sys.argv
if len(argv) == 2:
    """
    if first argument is passed save it as url
    """
    url = argv[1]

    if __name__ == '__main__':
        """
        execute only if run as main
        """
        try:
            with request.urlopen(url) as response:
                data = response.read()
            dataString = data.decode('utf-8')
            print(dataString)
        except error.URLError as e:
            errorCode = e.getcode()
            print(f"Error code: {errorCode}")
