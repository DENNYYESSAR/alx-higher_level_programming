#!/usr/bin/python3
"""Defines unittests for rectangle.py."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_str(self):
        r = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 5/6 - 3/4")

if __name__ == '__main__':
    unittest.main()
