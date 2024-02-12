#!/usr/bin/python3
"""Defines unittests for square.py."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(10, 20, 30, 40)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)
        self.assertEqual(s.id, 40)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        s = Square(3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (6) 4/5 - 3")


if __name__ == '__main__':
    unittest.main()
