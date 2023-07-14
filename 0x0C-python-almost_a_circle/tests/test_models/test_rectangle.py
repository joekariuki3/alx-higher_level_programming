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
        cls.r3 = Rectangle(8, 7, 0, 0, 12)
        cls.r4 = Rectangle(3, 7)

    """test id None"""
    def test_None(self):
        self.assertTrue(type(TestRectangle.r1.id), int)
        self.assertTrue(type(TestRectangle.r2.id), int)

    """test id with int"""
    def test_int(self):
        self.assertEqual(TestRectangle.r3.id, 12)

    """test width value """
    def test_width_nonInt(self):
        with self.assertRaises(TypeError):
            TestRectangle.r4.width = "5"

    """test width value -ve """
    def test_width_negative(self):
        with self.assertRaises(ValueError):
            TestRectangle.r4.width = -1

    """test height value """
    def test_height_nonInt(self):
        with self.assertRaises(TypeError):
            TestRectangle.r4.height = "5"

    """test height value -ve """
    def test_height_negative(self):
        with self.assertRaises(ValueError):
            TestRectangle.r4.height = -1

    """test x value """
    def test_x_nonInt(self):
        with self.assertRaises(TypeError):
            TestRectangle.r3.x = "5"

    """test x value -ve """
    def test_x_negative(self):
        with self.assertRaises(ValueError):
            TestRectangle.r3.x = -1

    """test y value """
    def test_y_nonInt(self):
        with self.assertRaises(TypeError):
            TestRectangle.r3.y = "5"

    """test y value -ve """
    def test_y_negative(self):
        with self.assertRaises(ValueError):
            TestRectangle.r3.y = -1

    """ test area"""
    def test_area(self):
        self.assertEqual(TestRectangle.r3.area(), 56)
        self.assertEqual(TestRectangle.r2.area(), 20)


if __name__ == "__main__":
    unittest.main()
