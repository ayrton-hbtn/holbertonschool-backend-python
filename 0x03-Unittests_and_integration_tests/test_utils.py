#!/usr/bin/env python3
"""Testing utils.access_nested_map method"""

from parameterized import parameterized
import unittest
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class to test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """method to test access_nested_map"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """Checks that a KeyError is raised when wrong inputs are passed"""
        with self.assertRaises(KeyError) as e:
            self.assertEqual(access_nested_map(map, path), e.exception)
