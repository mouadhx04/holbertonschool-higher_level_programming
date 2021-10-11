#!/usr/bin/python3
"""
rebel class
"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, other):
        """
        Eq function
        Args:
                other(int): number to operate on
        Returns:
    the inverted operator !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Ne function
        Args:
                other(int): number to operate on
        Returns:
    the inverted operator ==
        """
        return super().__eq__(other)
