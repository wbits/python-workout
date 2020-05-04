import unittest
import os


def last_line(file_name: str) -> str:
    with open(file_name, 'r') as f:
        for line in f:
            pass

    return line


def first_line(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.readline()


def digit_word_count(line: str) -> int:
    result = 0
    for word in line.split(' '):
        if word.isdigit():
            result += int(word)

    return result


def summing_file_content(file_name: str) -> int:
    with open(file_name, 'r') as f:
        return sum(map(digit_word_count, f))


def vowel_count(string: str, result: dict = None) -> dict:
    if result is None:
        result = {}
    for char in string:
        c = char.lower()
        if c in 'aeiou':
            result.update({c: result.get(c, 0) + 1})

    return result


def vowel_count_file_content(file_name: str) -> dict:
    result = {}
    with open(file_name, 'r') as f:
        for line in f:
            result = vowel_count(line, result)

    return result


class MyFileSystemTestCase(unittest.TestCase):
    FILE_NAME = 'test_file'

    def tearDown(self) -> None:
        os.remove(self.FILE_NAME)

    def test_read_last_line(self) -> None:
        self.__write_file("""
        First line
        Second line
        Last line
        """)

        self.assertEqual('Last line \n', last_line(self.FILE_NAME))

    def test_read_first_line(self) -> None:
        self.__write_file("""
        First line
        Second line
        Last line
        """)

        self.assertEqual('First line \n', first_line(self.FILE_NAME))

    def test_it_sums_words_that_only_contain_digits(self) -> None:
        self.__write_file("""
        The standard chunk of Lorem Ipsum used since the 1500s 
        is reproduced below for those interested. Sections 1.10.32 
        and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also 
        reproduced in their exact original form, accompanied by English versions from the 
        1914 translation by H. Rackham.
        """)

        self.assertEqual(1914, summing_file_content(self.FILE_NAME))

    def test_it_counts_vowels(self) -> None:
        self.__write_file("""
        Apple
        Banana
        Orange
        """)

        self.assertEqual({'a': 5, 'e': 2, 'o': 1}, vowel_count_file_content(self.FILE_NAME))

    @staticmethod
    def __write_file(text: str):
        with open(MyFileSystemTestCase.FILE_NAME, 'w') as file:
            for line in text.split('\n'):
                if line.strip():
                    file.write(f'{line.strip()} \n')
