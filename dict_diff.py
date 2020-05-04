import unittest
from typing import Callable


def dict_diff(a: dict, b: dict) -> dict:
    result = {}
    ab_keys = a.keys() | b.keys()
    for key in ab_keys:
        a_value = a.get(key, None)
        b_value = b.get(key, None)
        if a_value != b_value:
            result.update({key: [a_value, b_value]})

    return result


def dict_merge(*dictionaries: dict) -> dict:
    result = {}
    for d in dictionaries:
        result.update(d)

    return result


def dict_ed(*args: str) -> dict:
    result = {}
    key = None
    for arg in args:
        if not key:
            key = arg
            continue
        result.update({key: arg})
        key = None

    return result


def dict_partition(dictionary: dict, f: Callable) -> tuple:
    result1 = {}
    result2 = {}
    for key in dictionary:
        if f(key):
            result1.update({key: dictionary.get(key)})
            continue

        result2.update({key: dictionary.get(key)})

    return result1, result2


class MyTestCase(unittest.TestCase):
    def test_1(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual({}, dict_diff(d1, d1))

    def test_2(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'c': 4}
        self.assertEqual({'c': [3, 4]}, dict_diff(d1, d2))

    def test_3(self):
        d1 = {'a': 1, 'b': 2, 'd': 3}
        d2 = {'a': 1, 'b': 2, 'c': 4}
        self.assertEqual({'c': [None, 4], 'd': [3, None]}, dict_diff(d1, d2))

    def test_4(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'd': 4}
        self.assertEqual({'c': [3, None], 'd': [None, 4]}, dict_diff(d1, d2))

    def test_dict_merge(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'d': 4, 'e': 5, 'f': 6}
        d3 = {'g': 7, 'h': 8, 'i': 8}
        d4 = {'g': 9, 'h': 10, 'i': 11}
        merged = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 9, 'h': 10, 'i': 11}
        self.assertEqual(merged, dict_merge(d1, d2, d3, d4))

    def test_a_dict_ed(self):
        expected = {'foo': 'bar', 'test': 'two', 'three': 'four'}
        self.assertEqual(expected, dict_ed('foo', 'bar', 'test', 'two', 'three', 'four'))

    def test_dict_partition(self):
        original = {'one': 'one', 'two': 'two', 'three': 'three'}
        expected = ({'one': 'one'}, {'two': 'two', 'three': 'three'})
        self.assertEqual(expected, dict_partition(original, lambda string: string[0] in 'aeiouAEIOU'))


if __name__ == '__main__':
    unittest.main()
