#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer(list=[0, 4, 9, 6]), 9)
        self.assertEqual(max_integer(list=[1.1]), 1.1)
        self.assertEqual(max_integer(list=[0, -4, -9, -6]), 0)
        self.assertEqual(max_integer(list=[-4, -9, -6]), -4)
        self.assertIsNone(max_integer(list=[]))
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(list=[0, 4, 9, "Hello"])


if __name__ == "__main__":
    unittest.main()
