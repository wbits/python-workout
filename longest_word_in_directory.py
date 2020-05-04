import unittest
import shutil
import os


def longest_word(directory: str) -> str:
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            for line in f:
                for word in line.split():
                    if len(word) > len(result):
                        result = word

    return result


class MyTestCase(unittest.TestCase):
    TEST_DIR = 'test_dir'

    def setUp(self) -> None:
        os.mkdir(self.TEST_DIR)
        with open(os.path.join(self.TEST_DIR, 'f1'), 'w') as f1:
            f1.write(self.__f1())
        with open(os.path.join(self.TEST_DIR, 'f2'), 'w') as f2:
            f2.write(self.__f2())
        with open(os.path.join(self.TEST_DIR, 'f3'), 'w') as f3:
            f3.write(self.__f3())

    def tearDown(self) -> None:
        shutil.rmtree(self.TEST_DIR)

    def test_something(self):
        self.assertEqual('Policeman', longest_word(self.TEST_DIR))

    @staticmethod
    def __f1() -> str:
        return """Banana
Apple
Orange
        """

    @staticmethod
    def __f2() -> str:
        return """House
Building
Tower
        """

    @staticmethod
    def __f3() -> str:
        return """Policeman
Fireman
Doctor
        """


if __name__ == '__main__':
    unittest.main()
