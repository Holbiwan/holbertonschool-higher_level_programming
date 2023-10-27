#!/usr/bin/python3
"""import"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Class Rectangle tests"""

    def test_rectangle_creation_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_creation_2(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_creation_3(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_creation_4(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(TypeError, Rectangle, width='2')
        self.assertRaises(TypeError, Rectangle, width=float('NaN'))
        self.assertRaises(TypeError, Rectangle, width=float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, height='abc')
        self.assertRaises(TypeError, Rectangle, 1, 1, x={})
        self.assertRaises(TypeError, Rectangle, 1, 1, y=2.5)

    
      def test_rectangle_to_dictionary_exists(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        result = {
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
            'id': 5
        }
        self.assertEqual(rect_dict, result)

    def test_rectangle_update_exists_1(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_2(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_3(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_4(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        

if __name__ == "__main__":
    unittest.main()
