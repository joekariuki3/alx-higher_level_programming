#!/usr/bin/python3

"""
Get the unittest module
Get the Rectangle class from models/rectangle.py
Get patch from inittest.moc
get StringIO from io
"""

import unittest
from unittest.mock import patch
from io import StringIO
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
        cls.r5 = Rectangle(2, 3, 2, 2)
        cls.r6 = Rectangle(4, 6, 2, 1, 12)

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

    """test Display"""
    def test_display(self):
        output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r5.display()
            self.assertEqual(fake_out.getvalue(), output)
        output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r5 = Rectangle(3, 2, 1, 0)
            TestRectangle.r5.display()
            self.assertEqual(fake_out.getvalue(), output)

    """test __str__"""
    def test_string(self):
        output = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)
        output = "[Rectangle] (1) 0/0 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(TestRectangle.r1)
            self.assertEqual(fake_out.getvalue(), output)

    """test update"""
    def test_update(self):
        output = "[Rectangle] (89) 4/8 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r6.update(89, 2, 3, 4, 8)
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)
        output = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TestRectangle.r6.update(x=1, height=2, y=3, width=4)
            print(TestRectangle.r6)
            self.assertEqual(fake_out.getvalue(), output)


if __name__ == "__main__":
    unittest.main()
