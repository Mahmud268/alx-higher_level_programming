#!/usr/bin/python3

"""Defines a square"""

class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """ Initializing new square

        """
        if not is isinstance(size, int):
            raise TypeError("size must be an integer"):

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        self.__size ** 2
