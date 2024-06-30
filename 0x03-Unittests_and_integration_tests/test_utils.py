#!/usr/bin/env python3
'''
Unit test and Integration tests
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''
    unit tests and Integration test using utittest
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
                ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        testing access_nested_map function
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
        test raising errors
        '''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    test class for get json
    '''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
        ])
    def test_get_json(self, url, expected):
        '''
        test method for the get json
        '''
        response = Mock()
        response.json.return_value = expected
        with patch('requests.get', return_value=response):
            responses = get_json(url)
            self.assertEqual(responses, expected)


class TestMemoize(unittest.TestCase):
    '''
    test memoize function class
    '''
    def test_memoize(self):
        '''
        test memoize method
        '''
        class TestClass:
            '''subclass of test_memoize'''
            def a_method(self):
                '''return 42'''
                return 42

            @memoize
            def a_property(self):
                '''set a method'''
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
