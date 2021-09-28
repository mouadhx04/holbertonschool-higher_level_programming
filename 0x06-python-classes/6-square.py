#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Square.
"""


class Square:
    """class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Method:
        Args:
            size (int): Length of a side of the square.
            position (tuple): positoin of the square in 2D space
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """get squar size
        Returns:
            Private instance attribute __size
          """
        return self.__size

    @property
    def position(self):
        """get: __position
        Returns:
            Private instance attribute:
            The position of the square in 2D space
        """
        return self.__position

    @size.setter
    def size(self, value):
        """set of __size
        Args:
            value (int): the size of a side of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """set:__position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method:
        Area of the square.
        Returns:
            the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square:
        if 'size' is equal to 0, print an empty line
        'position' should be use by using space -
        Don’t fill lines by spaces when position[1] > 0
        """

        if self.size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print(end="\n")
