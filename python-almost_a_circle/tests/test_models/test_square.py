#!/usr/bin/python3
"""import"""
import unittest
from models.square import Square
import os


class TestSquare(unittest.TestCase):
    """class Rectangle tests"""

    def test_Square_creation_1(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_Square_creation_2(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_creation_3(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_size_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_Square_x_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_Square_y_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_Square_creation_4(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_Square_size_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
 


if __name__ == "__main__":
    unittest.main()
