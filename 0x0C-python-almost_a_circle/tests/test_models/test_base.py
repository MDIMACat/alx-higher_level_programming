#!/usr/bin/python3
"""Test casees for Base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_one_obj_with_id(self):
        item = Base(12)
        self.assertEqual(12, item.id)

    def test_one_obj_without_id(self):
        item = Base()
        self.assertEqual(8, item.id)

    def test_multi_obj_with_id(self):
        item1 = Base(4)
        item2 = Base(5)
        item3 = Base(6)
        self.assertEqual(4, item1.id)
        self.assertEqual(5, item2.id)
        self.assertEqual(6, item3.id)

    def test_multi_obj_without_id(self):
        item4 = Base()
        item5 = Base()
        item6 = Base()
        self.assertEqual(5, item4.id)
        self.assertEqual(6, item5.id)
        self.assertEqual(7, item6.id)

    def test_multi_obj_mixed_id(self):
        item7 = Base()
        item8 = Base(23)
        item9 = Base(-34)
        self.assertEqual(4, item7.id)
        self.assertEqual(23, item8.id)
        self.assertEqual(-34, item9.id)

    def test_obj_with_neg_id(self):
        item10 = Base(-1)
        self.assertEqual(-1, item10.id)

    def test_multi_neg_id(self):
        item11 = Base(-12)
        item12 = Base(-13)
        item13 = Base(-14)
        self.assertEqual(-12, item11.id)
        self.assertEqual(-13, item12.id)
        self.assertEqual(-14, item13.id)

    def test_from_json_string_from_none(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_from_json_string_from_valid_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_str = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_input, output)

    def test_create_rectangle(self):
        rect = Rectangle(3, 5, 1, 1)
        obj_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**obj_dict)
        self.assertEqual("[Rectangle] (1) 1/1 - 3/5", str(rect2))

    def test_create_square(self):
        square = Square(3, 5, 1, 1)
        obj_dict = square.to_dictionary()
        square2 = Square.create(**obj_dict)
        self.assertEqual("[Square] (1) 5/1 - 3", str(square2))

    def test_to_json_string_with_argument_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual("[]", json_string)

    def test_to_json_string_with_empty_dictionary(self):
        json_string = Base.to_json_string({})
        self.assertEqual("[]", json_string)
