#!/usr/bin/python3
"""
This module defines a test class to perform
unit test on a function
"""
import unittest


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = _max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = _max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        result = _max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = _max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = _max_integer([-1, 3, -2, 4, -5])
        self.assertEqual(result, 4)
