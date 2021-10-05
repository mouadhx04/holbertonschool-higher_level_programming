#!/usr/bin/python3
"""
module to remove whitespace and add newlines to text
"""


def text_indentation(text):
    """ removes whitespace at start & end of each line and adds newlines"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in ['.', '?', ':']:
        text = text.replace(c, c + '\n\n')
    new = [line.strip() for line in text.split('\n')]
    new = '\n'.join(new)
    print(new, end='')
