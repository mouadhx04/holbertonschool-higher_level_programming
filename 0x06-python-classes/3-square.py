#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a Square Class """
    def __init__(self, size=0):
        """ defining the size of square """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ returns area of a square """
        return self.__size**2
