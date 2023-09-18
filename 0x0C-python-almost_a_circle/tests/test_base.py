#!/usr/bin/python3
"""Unit test for base module"""
import unittest
from module.base import Base


class Test_Base(unittest.TestCase):
    """Defines a class that evaluates different test cases"""

    def setUp(self):
        """Reset the counter before each test"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test method"""
        pass


