#!/usr/bin/python3
"""This module defines the add integer function
"""


def add_integer(a, b=98):
    """ Function that adds two string.
    Args:
        a (int): First addend.
        b (int): Second addend, set to zero.
    Returns:
        int: The return value. The sum
    """
    if(not isinstance(a, int) and not isinstance(a, float)) or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float) or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
