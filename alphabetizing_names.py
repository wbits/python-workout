import unittest


def alphabetize(people: list) -> str:
    result = ''
    ordered_list = sorted(people, key=lambda person: person['last'])
    for person in ordered_list:
        result += (person['last'],)


class TestAlphabetizingNames(unittest.TestCase):
    def test_it_prints_alphabetical(self):
        people = [
            {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
            {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
            {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
        ]

        expect = """Lerner, Reuven, reuven@lerner.co.il
        Putin, Vladimir, president@kremvax.ru
        Trump, Donald, president@whitehouse.gov"""

        self.assertEqual(expect, alphabetize(people))
