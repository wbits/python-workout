import unittest
from operator import itemgetter, attrgetter


class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class People:
    def __init__(self, *people: Person):
        self.people = people

    def add_person(self, person: Person):
        self.people += (person,)

    def by_age_desc(self):
        return sorted(self.people, key=attrgetter('age'), reverse=True)

    def by_age_asc(self):
        return sorted(self.people, key=attrgetter('age'))

    def by_last_name(self):
        return sorted(self.people, key=attrgetter('last_name', 'first_name'))


def vowel_count(some_string: str) -> int:
    c = 0
    for character in some_string:
        if character in 'aeiouAEIOU':
            c += 1

    return c


class SortedTest(unittest.TestCase):
    def test_it_sorts(self):
        self.assertEqual([1, 2, 3, 4, 5], sorted([5, 4, 3, 2, 1]))

    def test_list_sort(self):
        my_list = [5, 4, 3, 2, 1]
        s = sorted(my_list)
        my_list.sort()
        self.assertEqual(s, my_list)

    def test_it_sorts_keys(self):
        my_dict = {3: 'Foo', 2: 'Bar', 1: 'Zoo'}
        self.assertEqual([1, 2, 3], sorted(my_dict))

        my_dict = {'first_name': 'Dick', 'last_name': 'Brouwers'}
        self.assertEqual(['first_name', 'last_name'], sorted(my_dict))

        my_list = ['Talitha', 'Jackie', 'Dick']
        self.assertEqual(['Dick', 'Jackie', 'Talitha'], sorted(my_list))

        my_list = ['Talitha', 'jackie', 'dick']
        self.assertEqual(['dick', 'jackie', 'Talitha'], sorted(my_list, key=str.lower))

    def test_it_sorts_complex_structures(self):
        talitha = {'first_name': 'Talitha', 'last_name': 'Ringers', 'age': 41}
        dick = {'first_name': 'Dick', 'last_name': 'Brouwers', 'age': 54}
        jackie = {'first_name': 'Jackie', 'last_name': 'Brouwers', 'age': 11}
        people = [jackie, talitha, dick]

        people_ordered_by_first_name = sorted(people, key=lambda person: person['first_name'])
        self.assertEqual([dick, jackie, talitha], people_ordered_by_first_name)

        people_ordered_by_age = sorted(people, key=lambda person: person['age'])
        self.assertEqual([jackie, talitha, dick], people_ordered_by_age)

        people_ordered_by_last_name_and_first_name_secondly = sorted(people, key=itemgetter('last_name', 'first_name'))
        self.assertEqual([dick, jackie, talitha], people_ordered_by_last_name_and_first_name_secondly)

    def test_it_sorts_objects(self):
        dick = Person('Dick', 'Brouwers', 54)
        jackie = Person('Jackie', 'Brouwers', 11)
        talitha = Person('Talitha', 'Ringers', 41)
        people = People()
        people.add_person(dick)
        people.add_person(jackie)
        people.add_person(talitha)

        self.assertEqual([dick, talitha, jackie], people.by_age_desc())
        self.assertEqual([jackie, talitha, dick], people.by_age_asc())
        self.assertEqual([dick, jackie, talitha], people.by_last_name())

    def test_it_counts_vowels(self):
        self.assertEqual(12, vowel_count('itCountsTheNumberOfVowelsInAString'))

    def test_it_sorts_by_highest_number_of_vowels(self):
        self.assertEqual(['foobar', 'foo', 'yo'], sorted(['foobar', 'yo', 'foo'], key=vowel_count, reverse=True))
        self.assertEqual(['yo', 'foo', 'foobar'], sorted(['foobar', 'yo', 'foo'], key=vowel_count))

    def test_it_sorts_by_absolute_value(self):
        self.assertEqual([1, -2, -3, 4], sorted([-3, -2, 1, 4], key=abs))

    def test_it_sorts_by_the_sum_of_each_inner_lists_numbers(self):
        sequence = [[4, 5, 6], [1, 2, 3], [7, 8, 9]]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, sorted(sequence, key=sum))
