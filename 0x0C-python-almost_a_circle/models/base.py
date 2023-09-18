#!/usr/bin/python3
"""The Base module"""


class Base:
    """The defination of the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): integer value

        Return:
            None

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
