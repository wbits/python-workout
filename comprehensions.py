import unittest
from typing import Callable


def make_str(*some_list: int, **kwargs) -> str:
    condition = kwargs.get('condition', lambda n: True)
    return ','.join(str(n) for n in some_list if condition(n))


def sum_str_numbers(string: str) -> int:
    return sum(int(n) for n in string.split() if n.isdigit())


def is_even(number: int) -> bool:
    return not number % 2


def flatten(nested_list: list) -> list:
    return [elem for single_list in nested_list for elem in single_list]


def flatten_odd_ints(nested_list: list) -> list:
    return [elem for single_list in nested_list for elem in single_list if not is_even(elem)]


def flip(dictionary: dict) -> dict:
    return {v: k for k, v in dictionary.items()}


def vowel_count(word: str) -> int:
    return len([char for char in word if char in 'aeiou'])


def vowel_count_all(sentence: str) -> dict:
    return {word: vowel_count(word) for word in sentence.split()}


def transform_values(func: Callable, dictionary: dict) -> dict:
    return {k: func(v) for k, v in dictionary.items()}


class MyTestCase(unittest.TestCase):
    def test_list_comprehension(self):
        self.assertEqual('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14', make_str(*range(15)))
        self.assertEqual('0,1,2,3,4,5,6,7,8,9', make_str(*range(15), condition=lambda n: n < 10))
        self.assertEqual('0,2,4,6,8,10,12,14', make_str(*range(15), condition=is_even))
        self.assertEqual('1,3,5,7,9,11,13', make_str(*range(15), condition=lambda n: n % 2))
        self.assertEqual(100, sum_str_numbers('10 abc 20 de44 30 55fg 40'))
        self.assertEqual([1, 2, 3, 4], flatten([[1, 2], [3, 4]]))
        self.assertEqual([1, 3], flatten_odd_ints([[1, 2], [3, 4]]))
        self.assertEqual({'a': 1, 'b': 2, 'c': 3}, flip({1: 'a', 2: 'b', 3: 'c'}))
        self.assertEqual(2, vowel_count('hello'))
        self.assertEqual({'this': 1, 'is': 1, 'an': 1, 'easy': 2, 'test': 1}, vowel_count_all('this is an easy test'))
        self.assertEqual({'a': 1, 'b': 4, 'c': 9}, transform_values(lambda x: x * x, {'a': 1, 'b': 2, 'c': 3}))


if __name__ == '__main__':
    unittest.main()
