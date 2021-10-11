#!/usr/bin/python3
"""is_kind_of_class:is a function that returns True
if the object is an instance of
or if the object is an instance of a class that inherited from
the specified class"""


def is_kind_of_class(obj, a_class):
    """obj:object
    a_class:class"""
    return isinstance(obj, a_class)
