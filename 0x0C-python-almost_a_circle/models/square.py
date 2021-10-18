#!/usr/bin/python3
'''Module for the class Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class that create a Squrare'''
    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(size, size, x, y, id)
        # pass same number of attributes to the super class

    @property
    def size(self):
        '''get the size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        '''set value to the size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    # why The setter should assign (in this order) the width and the height
    # - with the same value --> task 11

    def update(self, *args, **kwargs):
        '''assigns attributes'''
        if args:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                if idx == 1:
                    self.size = value
                if idx == 2:
                    self.x = value
                if idx == 3:
                    self.y = value
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        '''Returns:
                [Square] (<id>) <x>/<y> - <size>
        '''
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.size)

    def to_dictionary(self):
        '''Returns:
            the dictionary representation of a Square
        '''
        dict_ = {}
        dict_.update({"id": self.id,
                      "x": self.x,
                      "size": self.size,
                      "y": self.y
                      })
        return dict_
