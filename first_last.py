import unittest


def first_last(sequence: iter) -> iter:
    return sequence[:1] + sequence[-1:]


def even_odd_sums(sequence: iter) -> list:
    return [sum(sequence[::2]), sum(sequence[1::2])]


def plus_minus(sequence: iter) -> int:
    return sequence[0] + sum(sequence[1::2]) - sum(sequence[::2][1:])


def my_zip(*iterables: iter) -> list:
    result = []
    for iterable in iterables:
        for i in range(0, len(iterable)):
            if len(result) <= i:
                result.append(())

            result[i] += (iterable[i],)

    return result


class TestFirstLast(unittest.TestCase):
    def test_first_last(self):
        self.assertEqual('14', first_last('1234'))
        self.assertEqual(('foo', 2), first_last(('foo', 'bar', 1, 2)))
        self.assertEqual(['foo', 'bar'], first_last(['foo', 'test', 'bar']))

    def test_even_odd_sums(self):
        self.assertEqual([9, 6], even_odd_sums([1, 2, 3, 4, 5]))
        self.assertEqual([35, 60], even_odd_sums((25, 20, 10, 40)))

    def test_plus_minus(self):
        self.assertEqual(15, plus_minus([10, 15, 5, 15, 20]))
        self.assertEqual(40, plus_minus([10, 10, 1, 11, 1, 11]))
        self.assertEqual(11, plus_minus([10, 1]))

    def test_my_zip(self):
        self.assertEqual([(10, 'a'), (20, 'b'), (30, 'c')], my_zip([10, 20, 30], 'abc'))
