#!/usr/bin/python3

"""A defination of class Mylist that inherits from the class list"""

class MyList(List):
    """A defination of class mylist that inherits from the class list."""

    def print_sorted(self):
        """Print the element of the list in assending order"""
        return sorted(self)
