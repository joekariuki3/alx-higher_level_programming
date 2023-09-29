#!/usr/bin/python3

"""
get required modules
"""
import requests
import sys

argv = sys.argv

if len(argv) == 2:
    url = argv[1]

    if __name__ == '__main__':
        """
        execute onlu if run as main

        script that takes url 1st arg
        then  displays the response body
        if 400 and above print status code
        """
        resp = requests.get(url)
        if resp.ok:
            body = resp.text
            print(body)
        else:
            code = resp.status_code
            print(f"Error code: {code}")
