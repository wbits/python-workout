import unittest


class MyClass:
    def __init__(self, name: str):
        self.__name = name

    def __call__(self) -> str:
        return f'I call you {self.__name}'

    def __str__(self) -> str:
        return f'I print {self.__name}'


class MyTestCase(unittest.TestCase):
    def test_it_contains_unique_values(self):
        numbers = [1, 2, 3, 3, 4, 4, 5]
        unique_numbers = set(numbers)

        self.assertTrue(len(numbers) is 7)
        self.assertTrue(len(unique_numbers) is 5)

    def test_it_can_be_created_in_different_ways(self):
        numbers = [1, 2, 3, 3, 4, 4, 5]
        unique_numbers = set(numbers)

        self.assertEqual(unique_numbers, {*numbers})

        new_set = set()
        new_set.update(numbers)
        self.assertEqual(unique_numbers, new_set)

        new_set = set()
        for n in numbers:
            new_set.add(n)
        self.assertEqual(unique_numbers, new_set)

    def test_is_call_invoke(self):
        foo = MyClass('foo')
        self.assertEqual('I call you foo', foo())
        self.assertEqual('I print foo', str(foo))


if __name__ == '__main__':
    unittest.main()
