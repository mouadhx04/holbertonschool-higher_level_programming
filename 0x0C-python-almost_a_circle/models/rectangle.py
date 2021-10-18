#!/usr/bin/python3
'''Module for the class Rectangle
'''


from models.base import Base


class Rectangle(Base):
    '''class that create a Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get Rectabgle width'''
        return self.__width

    @property
    def height(self):
        '''get Rectangle height'''
        return self.__height

    @property
    def x(self):
        '''get the x size'''
        return self.__x

    @property
    def y(self):
        '''get the y size'''
        return self.__y

    @width.setter
    def width(self, value):
        '''set the width value'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''set the height value'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        '''set the x value'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''set the y value'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''public method
        Return:
            the area of the Rectangle
        '''
        return self.width * self.height

    def display(self):
        '''print the Rectangle'''
        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")
            print()
    # print("#" for _ in range(self.__height) for _ in range(self.__width))

    def __str__(self):
        '''Returns:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        if self.__class__.__name__ == "Square":
            return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                 self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)
        else:
            return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                    self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)

    def display(self):
        '''print a Rectangle instance with char #'''
        print("\n" * self.y, end="")
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        '''update attributes value'''
        if args:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.width = value
                elif idx == 2:
                    self.height = value
                elif idx == 3:
                    self.x = value
                elif idx == 4:
                    self.y = value
            return
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
            return

    def to_dictionary(self):
        '''Returns:
            the dictionary representation of a Rectangle
        '''
        dict_ = {}
        dict_.update({"x": self.x,
                      "y": self.y,
                      "id": self.id,
                      "height": self.height,
                      "width": self.width
                      })
        return dict_
