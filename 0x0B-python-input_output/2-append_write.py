#!/usr/bin/python3
'''Append a text
'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file
    Returns:
        the number of characters added
    '''
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
