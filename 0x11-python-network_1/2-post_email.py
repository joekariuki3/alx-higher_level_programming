#!/usr/bin/python3

"""
import required headers
urllib.request
urllib.parse
sys
"""
import urllib.request as request
import urllib.parse as parse
import sys

argv = sys.argv
if len(argv) == 3:
    """
    if 2 arguments are passes 1st url 2nd email
    """
    url = argv[1]
    email = argv[2]

    if __name__ == '__main__':
        """
        if executed as main
        """
        # creat a dictionary of data to pass to server
        values = {'email': email}

        # format the data as required to be passed to the server
        valuesEncoded = parse.urlencode(values)

        # convert the data drom string to bytes
        valuesBytes = valuesEncoded.encode('ascii')

        # attach the data to the url
        finalUrl = request.Request(url, valuesBytes)

        with request.urlopen(finalUrl) as response:
            data = response.read()
        dataString = data.decode('utf-8')
        print(dataString)
