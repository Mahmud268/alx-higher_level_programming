#!/usr/bin/python3

"""
    Defines a class method
"""

def is_kind_of_class(obj, a_class):
    """A method that compares an object.
    Args:
        obj (any): The the object to be check.
        a_class (type): The class to match the type of the object to.

    Returns: 
        True - if is an instance, False - if otherwise
    """

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
