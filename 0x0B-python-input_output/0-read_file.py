#!/usr/bin/python3
'''Open a new file
'''


def read_file(filename=""):
    '''Open a file using with
    '''
    with open(filename) as file:
        for line in file:
            print(line, end="")
