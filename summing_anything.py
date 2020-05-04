import unittest


def my_sum(*args):
    if not args:
        return args
    result = args[0]
    for v in args[1:]:
        result = result + v

    return result


def my_sum_bigger_than(n, *args):
    t = ()
    for item in args:
        if item > n:
            t += (item,)

    return my_sum(*t)


def sum_numeric(*args):
    t = ()
    for item in args:
        try:
            t += (int(item),)
        except ValueError:
            continue

    return my_sum(*t)


class TestMySum(unittest.TestCase):
    def test_it_sums(self):
        self.assertEqual(5, my_sum(2, 3))
        self.assertEqual(9, my_sum(2, 3, 4))
        self.assertEqual('abcdef', my_sum('abc', 'def'))
        self.assertEqual([1, 2, 3, 4, 5, 6], my_sum([1, 2, 3], [4, 5, 6]))
        self.assertEqual('.', my_sum('.'))
        self.assertEqual((), my_sum())

    def test_sum_bigger_than(self):
        self.assertEqual(50, my_sum_bigger_than(10, 5, 20, 30, 6))

    def test_sum_numeric(self):
        self.assertEqual(60, sum_numeric(10, 20, 'a', '30', 'bcd'))
