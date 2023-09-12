#!/usr/bin/python3
"""A module that contain a fuction that write file"""


def write_file(filename="", text=""):
    """A fuction that write a string to a filename.

    Args:
        filename: a to be written to.
        text: a text to be added to file.

    Returns:
        None
    """

        with open(filename, "w", encoding="utf-8") as f:
            return (f.write(text))
