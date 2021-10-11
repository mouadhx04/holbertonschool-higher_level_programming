#!/usr/bin/python3
"""inherits_from:returns True if the object is an
instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """obj:object
    a_class:class
    return returns True if the object is an instance of a class """
    return isinstance(obj, a_class) and type(obj) is not a_class
