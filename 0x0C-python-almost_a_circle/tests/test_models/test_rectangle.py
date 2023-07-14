#!/usr/bin/python3

"""
Get the unittest module
Get the Rectangle class from models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle

"""start of unittest class """


class TestRectangle(unittest.TestCase):

    """set up function"""
    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestRectangle.r1.id), int)
        self.assertTrue(type(TestRectangle.r2.id), int)

    """test id with int"""
    def test_int(self):
        self.assertEqual(TestRectangle.r3.id, 12)


if __name__ == "__main__":
    unittest.main()
