#!/usr/bin/python3

"""Contain function that read a text file"""

def read_file(filename=""):
    """A defination of function that read a text file"""

    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read)
