#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialising a new Square.
        Args:
            size (int): The size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
