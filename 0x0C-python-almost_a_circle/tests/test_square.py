#!/usr/bin/python3
"""Test Class for square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_full_init_id(self):
        sqr = Square(12, 2, 2, 12)
        self.assertEqual(12, sqr.id)

    def test_full_init_width(self):
        sqr = Square(12, 2, 2, 12)
        self.assertEqual(12, sqr.width)

    def test_full_init_x(self):
        sqr = Square(12, 2, 2, 12)
        self.assertEqual(2, sqr._x)

    def test_full_init_y(self):
        sqr = Square(12, 2, 2, 12)
        self.assertEqual(2, sqr._y)

    def test_no_id(self):
        sqr = Square(2)
        self.assertEqual(32, sqr.id)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            sqr = Square("10", 2, 1, 23)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            sqr = Square(10, "2", 1, 23)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            sqr = Square(10, 2, "1", 23)

    def test_incorrect_value_width(self):
        with self.assertRaises(ValueError):
            sqr = Square(-10, 2, 1, 23)

    def test_incorrect_value_x(self):
        with self.assertRaises(ValueError):
            sqr = Square(10, -2, 1, 23)

    def test_incorrect_value_y(self):
        with self.assertRaises(ValueError):
            sqr = Square(10, 2, -1, 23)

    def test_neg_id(self):
        sqr = Square(10, 2, 1, -23)
        self.assertEqual(-23, sqr.id)

    def test_update_with_three_args(self):
        sqr = Square(8)
        sqr.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(sqr))

    def test_update_with_two_args(self):
        sqr = Square(8)
        sqr.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(sqr))

    def test_update_with_four_args(self):
        sqr = Square(8)
        sqr.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(sqr))

    def test_update_with_one_arg(self):
        sqr = Square(8)
        sqr.update(10)
        self.assertEqual("[Square] (10) 0/0 - 8", str(sqr))

    def test_to_dictionary_only_size(self):
        sqr = Square(10)
        rep = sqr.to_dictionary()
        self.assertEqual({"id": 34, "size": 10, "x": 0, "y": 0}, rep)

    def test_to_dictionary_no_id(self):
        sqr = Square(10, 9, 8)
        rep = sqr.to_dictionary()
        self.assertEqual({"id": 33, "size": 10, "x": 9, "y": 8}, rep)

    def test_to_dictionary_all_attributes(self):
        sqr = Square(10, 1, 2, 3)
        rep = sqr.to_dictionary()
        self.assertEqual({"id": 3, "size": 10, "x": 1, "y": 2}, rep)

    def test_update_with_4_args(self):
        sqr = Square(3)
        sqr.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(sqr))

    def test_update_with_3_args(self):
        sqr = Square(6)
        sqr.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(sqr))

    def test_update_with_2_args(self):
        sqr = Square(5)
        sqr.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(sqr))

    def test_update_with_1_arg(self):
        sqr = Square(5)
        sqr.update(23)
        self.assertEqual("[Square] (23) 0/0 - 5", str(sqr))
