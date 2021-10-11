#!/usr/bin/python3
"""is_same_class:a function that returns True if the object
is exactly an instance
of the specified class
otherwise False."""


def is_same_class(obj, a_class):
    """the object is exactly an instance of the specified class
    obj: object
    a_class: class
    """
    return type(obj) is a_class
