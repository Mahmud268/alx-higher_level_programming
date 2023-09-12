#!/usr/bin/python3

"""Contain function that read a text file"""

def read_file(filename=""):
    """A defination of function that read UTF8 text file and print it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end"")
