#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """A definition of a function that reads a text file"""

    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read)

