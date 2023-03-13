#!/usr/bin/python3

def no_c(my_string):
    """
    Return a copy of my string without c or C
    Args:
        my_string - the string to filter

    """
    new_string = ''
    for char in my_string:
        if char is not in ['c', 'C']:
            new_string += char
    return new_string
