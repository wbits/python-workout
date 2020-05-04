import datetime
import unittest


class Calendar:
    def __init__(self, birthdays: dict):
        self.__birthdays = birthdays

    def age_in_days(self, name: str) -> int:
        timedelta = datetime.date.today() - self.__birthdays.get(name)

        return timedelta.days


class MyTestCase(unittest.TestCase):
    def test_it_calculates_age_in_days(self):
        some_birthday = datetime.date.today() - datetime.timedelta(days=5)
        calendar = Calendar({
            'test': some_birthday,
            'Dick': datetime.date(1965, 9, 17)
        })

        self.assertEqual(5, calendar.age_in_days('test'))
        self.assertTrue(calendar.age_in_days('Dick') > 19900)
