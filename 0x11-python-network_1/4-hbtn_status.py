#!/usr/bin/python3

"""
get the rquired models : requests
"""
import requests

if __name__ == '__main__':
    """
    execute only if run as main

    script to fetch a url
    """
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")
