#!/usr/bin/python3
"""Test class for Rectangle Class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_full_init_id(self):
        rect = Rectangle(10, 2, 1, 23, 1)
        self.assertEqual(1, rect.id)

    def test_full_init_width(self):
        rect = Rectangle(10, 2, 1, 23, 1)
        self.assertEqual(10, rect._width)

    def test_full_init_height(self):
        rect = Rectangle(10, 2, 1, 23, 1)
        self.assertEqual(2, rect._height)

    def test_full_init_x(self):
        rect = Rectangle(10, 2, 1, 23, 1)
        self.assertEqual(1, rect._x)

    def test_full_init_y(self):
        rect = Rectangle(10, 2, 1, 23, 1)
        self.assertEqual(23, rect._y)

    def test_no_id(self):
        rect = Rectangle(23, 4, 16, 2)
        self.assertEqual(17, rect.id)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("10", 2, 1, 23, 1)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "2", 1, 23, 1)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 2, "1", 23, 1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 2, 1, "23", 1)

    def test_incorrect_value_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 2, 1, 23, 1)

    def test_incorrect_value_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -2, 1, 23, 1)

    def test_incorrect_value_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 2, -1, 23, 1)

    def test_incorrect_val_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 2, 1, -23, 1)

    def test_no_args_passed(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_1_args_passed(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(23)

    def test_area_two_args(self):
        rect = Rectangle(4, 5)
        self.assertEqual(20, rect.area())

    def test_area_with_id(self):
        rect = Rectangle(9, 2, 0, 0, 45)
        self.assertEqual(18, rect.area())

    def test_display(self):
        rect = Rectangle(2, 2)
        self.assertEqual(None, rect.display())

    def test_str(self):
        rect = Rectangle(5, 7, 8, 9, 10)
        self.assertEqual("[Rectangle] (10) 8/9 - 5/7", str(rect))

    def test_str_no_id(self):
        rect = Rectangle(5, 7, 8, 9)
        self.assertEqual("[Rectangle] (18) 8/9 - 5/7", str(rect))

    def test_display_xy_value(self):
        rect = Rectangle(2, 3, 2, 2)
        self.assertEqual(None, rect.display())

    def test_display_x_value(self):
        rect = Rectangle(3, 2, 2, 0)
        self.assertEqual(None, rect.display())

    def test_display_y_value(self):
        rect = Rectangle(3, 2, 0, 2)
        self.assertEqual(None, rect.display())

    def test_display_neg_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 3, -2, -2)
            rect.display()

    def test_display_zero_value(self):
        rect = Rectangle(2, 2, 0, 0)
        self.assertEqual(None, rect.display())

    def test_display_char_value(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 3, "a", "b")
            rect.display()

    def test_update_with_one_arg(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_with_two_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_with_three_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_update_with_four_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

    def test_update_with_five_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_update_with_args_only(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(5, 20, 15, 7, 8)
        self.assertEqual("[Rectangle] (5) 7/8 - 20/15", str(rect))

    def test_update_with_kwargs_only(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(width=20, id=5)
        self.assertEqual("[Rectangle] (5) 10/10 - 20/10", str(rect))

    def test_update_with_args_and_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(5, width=20, x=15)
        self.assertEqual("[Rectangle] (5) 15/10 - 20/10", str(rect))

    def test_update_with_empty_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update()
        self.assertEqual("[Rectangle] (23) 10/10 - 10/10", str(rect))

    def test_update_with_empty_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(id=5, width=20, height=15)
        self.assertEqual("[Rectangle] (5) 10/10 - 20/15", str(rect))

    def test_update_with_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 10, 10, 10)
            rect.update(invalid_arg=5, width=20, x=15)

    def test_to_dictionary_with_no_id_specified(self):
        rect = Rectangle(13, 3, 10, 10)
        rep = rect.to_dictionary()
        self.assertEqual({"id": 19, "width": 13, "height": 3, "x": 10,
                          "y": 10}, rep)

    def test_to_dictionary_with_only_width_height_specified(self):
        rect = Rectangle(12, 2)
        rep = rect.to_dictionary()
        self.assertEqual({"id": 20, "width": 12, "height": 2, "x": 0,
                          "y": 0}, rep)

    def test_to_dictionary_with_all_attributes(self):
        rect = Rectangle(12, 3, 5, 5, 12)
        rep = rect.to_dictionary()
        self.assertEqual({"id": 12, "width": 12, "height": 3, "x": 5,
                          "y": 5}, rep)
