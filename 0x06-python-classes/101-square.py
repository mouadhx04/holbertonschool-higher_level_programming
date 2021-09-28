#!/usr/bin/python3
"""
Square class.
"""


class Square:
    """Represents a square
    Attributes:
        __size (int): privat instance of the class square
        __position (tuple): privat instance of the class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the class object attributs
        Args:
            size (int): size of the square
            position (tuple): position of the shift
            Returns:
                None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            for k in range(self.__size + self.__position[0]):
                if k < self.__position[0]:
                    print(' ', end='')
                if k >= self.__position[0]:
                    print('#', end='')
            print('')

    def __str__(self):
        listx = []
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            listx = ''
            return listx

        for i in range(self.__position[1]):
            listx.append('\n')
        for j in range(self.__size):
            for k in range(self.__size + self.__position[0]):
                if k < self.__position[0]:
                    listx.append(" ")
                if k >= self.__position[0]:
                    listx.append('#')
            listx.append('\n')
        listx[len(listx)-1] = ''
        return ''.join(listx)

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
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
