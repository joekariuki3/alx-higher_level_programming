#!/usr/bin/python3

"""
import required modules: requests, sys
"""
import requests
import sys

if __name__ == '__main__':
    """
    only execute when run as main
    script to get json data depending on the passed value
    using post method
    """
    argv = sys.argv
    latter = ""
    if len(argv) == 2:
        latter = argv[1]
    values = {'q': latter}
    url = 'http://0.0.0.0:5000/search_user'
    resp = requests.post(url, data=values)
    jsonData = resp.json()
    if len(jsonData) == 0:
        print("No result")
    elif len(jsonData) > 0:
        id = jsonData.get('id')
        name = jsonData.get('name')
        print(f"[{id}] {name}")
    else:
        print("Not a valid JSON")
