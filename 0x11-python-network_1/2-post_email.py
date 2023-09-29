#!/usr/bin/python3

import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == '__main__':
    """
    if executed as main
    script that takes in a URL and an email
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    argv = sys.argv
    if len(argv) == 3:
        """
        if 2 arguments are passes
        1st url 2nd email
        """
        url = argv[1]
        email = argv[2]

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
