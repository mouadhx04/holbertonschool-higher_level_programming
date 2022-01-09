#!/usr/bin/python3
"""
Python script that fetches
https://intranet.hbtn.io/status
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
