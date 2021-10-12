#!/usr/bin/python3
'''Load from json file
'''
import json


def load_from_json_file(filename):
    '''Load from json file
        Returns:
    '''
    with open(filename, 'r') as file:
        return json.load(file)
