#!/usr/bin/python3

"""A defination of a function lookup"""

def  lookup(obj):
    """A fuction that returns a list of attributes and methods

    Args:
        obj (unknown): objects whode attributes and methods are to be returned

    """

    return (dir(obj))
