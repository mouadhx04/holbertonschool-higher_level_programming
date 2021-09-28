#!/usr/bin/python3
""" square class"""


class Square:
    """
    creates square
    """

    def __init__(self, size=0):
        """
        initializes square
        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        finds size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        validates size is an integer that is greater than zero
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        finds area of square
        Returns:
            area of square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        check if square is equal to other square
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        check if square is not equal to other square
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        check if square is greater than other square
        """
        return self.size > other.size

    def __lt__(self, other):
        """
        check if square is less than other square
        """
        return self.size < other.size

    def __ge__(self, other):
        """
        check if square is greater than or equal to other square
        """
        return self.size >= other.size

    def __le__(self, other):
        """
        check if square is less than or equal to other square
        """
        return self.size <= other.size
