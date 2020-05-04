import unittest
from collections import Counter


def most_repeating_letter(word: str) -> tuple:
    return Counter(word).most_common(1)[0]


def most_repeating_num(word: str) -> int:
    result = most_repeating_letter(word)
    return result[1]


def most_repeating_word(words):
    return max(words, key=most_repeating_num)


class MostRepeatingWordTest(unittest.TestCase):
    def test_it_counts_repeating_letters(self):
        word = 'example'
        self.assertEqual(('e', 2), most_repeating_letter(word))
        word = 'aabb'
        self.assertEqual(('a', 2), most_repeating_letter(word))

    def test_it_returns_a_word_with_most_repeating_letters(self):
        words = ['this', 'is', 'an', 'elementary', 'test', 'example']
        self.assertEqual('elementary', most_repeating_word(words))
