#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with regular integer lists."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4]), -4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_mixed_list(self):
        """Test with lists containing mixed data types."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'a'])

    def test_float_list(self):
        """Test with lists containing floating-point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.5, 3.5, 4.5, 2.5]), 4.5)
        self.assertEqual(max_integer([4.5]), 4.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)
        self.assertEqual(max_integer([-1.5, -3.5, -4.5, -2.5]), -1.5)
        self.assertEqual(max_integer([-4.5]), -4.5)


if __name__ == '__main__':
    unittest.main()
