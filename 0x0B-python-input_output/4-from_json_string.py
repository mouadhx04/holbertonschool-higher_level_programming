#!/usr/bin/python3
'''JSON object
'''
import json


def from_json_string(my_str):
    '''Returns:
            Python object
    '''
    return json.loads(my_str)
