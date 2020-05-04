import unittest
import os


def translate_pig_latin(word: str) -> str:
    if word[0] in 'aeiouAEIOU':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'


def translate_file_to_pig_latin(filename: str) -> str:
    with open(filename) as file:
        return ' '.join(translate_pig_latin(word) for line in file for word in line.split())


class MyTestCase(unittest.TestCase):
    PATH = 'test_file'

    def setUp(self) -> None:
        with open(self.PATH, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self) -> None:
        os.remove(self.PATH)

    def test_something(self):
        self.assertEqual('hisTay isway away esttay ile.fay', translate_file_to_pig_latin(self.PATH))


if __name__ == '__main__':
    unittest.main()
