#!/usr/bin/python3

"""
get required modules
"""
import requests
import sys

argv = sys.argv

if len(argv) == 3:
    url = argv[1]
    email = argv[2]

    if __name__ == '__main__':
        """
        execute onlu if run as main

        script that takes url 1st arg n email 2nd arg
        pass the email to the url
        then  displays the response body
        """
        values = {'email': email}
        resp = requests.post(url, data=values)
        body = resp.text
        print(body)
