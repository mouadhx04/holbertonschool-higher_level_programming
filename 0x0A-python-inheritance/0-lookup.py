#!/usr/bin/python3
""" avialable attributes and methods of an object """


def lookup(obj):
    """
    Returns the list of avialable attributes and methods of an object
    Args:
    obj (object): the object to look up.
    Return (List): list of objects.
"""
    return dir(obj)
