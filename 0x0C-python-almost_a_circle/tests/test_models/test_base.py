#!/usr/bin/python3

"""
Get the unittest module
Get the base class from models/base.py
"""

import unittest
from models.base import Base

"""start of unittest class """


class TestBase(unittest.TestCase):

    """set up function"""
    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base(57)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestBase.b1.id), int)

    """test id with int"""
    def test_int(self):
        self.assertEqual(TestBase.b2.id, 57)


if __name__ == "__main__":
    unittest.main()
