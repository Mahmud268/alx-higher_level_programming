#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Creates a copy of a list and replaces the value at the specified index with a new value.

    Args:
        my_list (list): The original list.
        idx (int): The index of the value to replace.
        element (any): The new value to replace the old value with.

    Returns:
        list: A copy of the original list with the value at the specified index replaced with the new value. If the index is out of range, the original list is returned.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list

