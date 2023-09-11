#!/usr/bin/python3

"""
    A module for is same class method
"""

def is_same_class(obj, a_class):
    """To check if an object is exactly an instance of a class.

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class type to validate.

    Returns:
        bool: True is the object is an instance is an instance of the class, Otherwise Fales

    """

    return isinstance(obj, a_class)
