#!/usr/bin/python3
""" Square class"""


class Square:
    """ This is a Square Class """
    def __init__(self, size=0):
        """ defining the size of square """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ returns area of a square """
        return self.__size**2

    @property
    def size(self):
        """ returns size variable of Square class instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square class instance """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
