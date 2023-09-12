#!/usr/bin/python3
"""Defines the string to json objects"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
