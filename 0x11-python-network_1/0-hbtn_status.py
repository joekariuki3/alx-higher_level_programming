#!/usr/bin/python3

"""
import urllib.request module
"""
import urllib.request

if __name__ == '__main__':
    """
    if this module is imported
    dont execute
    if it is run as main execute

    script to fetch a url and display its body
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        dataString = data.decode('utf8')
    print("Body response:")
    print(f"\t - type: {type(data)}")
    print(f"\t - content: {data}")
    print(f"\t - utf8 content: {dataString}")
