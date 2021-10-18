#!/usr/bin/python3
'''module for base class
'''


import json


class Base:
    '''Manage id attribute in all future classes
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''the init method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert to a json string'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to json file'''
        if list_objs is None:
            list_objs = []
        l = []
        for obj in list_objs:
            l.append(cls.to_dictionary(obj))
        with open('{}.json'.format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        '''convert from json string'''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create insctance'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy
