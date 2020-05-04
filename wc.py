import unittest
import os


class Count:
    def __init__(self, filename: str):
        self.__filename = filename

    def __enter__(self):
        self.__file = open(self.__filename)
        self.__counters = {'l': 0, 'w': 0, 'c': 0, 'u': 0}
        unique_words = set()

        for line in self.__file:
            self.__counters['l'] += 1
            self.__counters['w'] += len(line.split())
            self.__counters['c'] += len(line)
            unique_words.update(line.split())

        self.__counters.update({'u': len(unique_words)})

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def words(self) -> int:
        return self.__counters.get('w', 0)

    def unique_words(self) -> int:
        return self.__counters.get('u', 0)

    def lines(self) -> int:
        return self.__counters.get('l', 0)

    def characters(self) -> int:
        return self.__counters.get('c', 0)


class MyTestCase(unittest.TestCase):
    PATH = 'test_file'

    def setUp(self) -> None:
        with open(self.PATH, 'w') as f:
            f.write("""This is a test file.

It contains 28 words and 20 different words.

It also contains 165 characters.

It also contains 11 lines.

It is also self-referential.

Wow!
""")

    def tearDown(self) -> None:
        os.remove(self.PATH)

    def test_it_counts(self):
        with Count(self.PATH) as count:
            self.assertEqual(28, count.words())
            self.assertEqual(20, count.unique_words())
            self.assertEqual(11, count.lines())
            self.assertEqual(165, count.characters())


if __name__ == '__main__':
    unittest.main()
