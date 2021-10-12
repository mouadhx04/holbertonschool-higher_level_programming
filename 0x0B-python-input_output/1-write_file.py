#!/usr/bin/python3
'''Write a text to a file
'''


def write_file(filename="", text=""):
    '''Write to a file using with
    '''
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
