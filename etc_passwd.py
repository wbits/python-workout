import unittest
import csv
import os


class SystemUsers:
    def __init__(self, filename: str):
        self.__filename = filename
        self.__users = {}

    def __enter__(self):
        self.__file = open(self.__filename)
        for line in self.__file:
            if line.startswith('#') or not line.strip():
                continue
            user_info = line.split(':')
            self.__users.update({user_info[0]: user_info[2]})

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def as_dict(self) -> dict:
        return self.__users

    def as_csv(self) -> None:
        with open('test.csv', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            for user, id in self.__users.items():
                writer.writerow((user, id))


def starts_with_or_not_strip(string: str):
    return string.startswith('#') or not string.strip()


class MyTestCase(unittest.TestCase):
    PWD_PATH = '/etc/passwd'

    def test_it_contains_users(self):
        with SystemUsers(self.PWD_PATH) as systemUsers:
            d = systemUsers.as_dict()

        self.assertEqual('0', d['root'])

    def test_if_starts_with_or_not_strip(self):
        f = starts_with_or_not_strip
        self.assertTrue(f('#hello'))
        self.assertTrue(f(' '))
        self.assertFalse(f(' foo '))

    def test_it_writes_a_csv_file(self):
        with SystemUsers(self.PWD_PATH) as systemUsers:
            systemUsers.as_csv()
            d = systemUsers.as_dict()
        with open('test.csv') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                self.assertEqual(d[row[0]], row[1])

    def tearDown(self) -> None:
        if os.path.exists('test.csv'):
            os.remove('test.csv')


if __name__ == '__main__':
    unittest.main()
