#!/usr/bin/env python3
"""Testing utils.access_nested_map method"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """class to test access_nested_map()"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """method to test access_nested_map return value"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """Checks that a KeyError is raised when wrong inputs are passed"""
        with self.assertRaises(KeyError) as e:
            self.assertEqual(access_nested_map(map, path), e.exception)


class TestGetJson(unittest.TestCase):
    """class to test get_json()"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method to test get_json method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.assert_called_once()
