import unittest
import operator
import functools


class InvalidOperator(Exception):
    pass


class NonNumericalValue(Exception):
    pass


class Calculator:
    @staticmethod
    def prefix(command: str) -> float:
        digits = command.split()
        return Calculator.__calculate(digits.pop(0), *map(Calculator.__convert_number, digits))

    @staticmethod
    def postfix(command: str) -> float:
        digits = command.split()
        return Calculator.__calculate(digits.pop(), *map(Calculator.__convert_number, digits))

    @staticmethod
    def __calculate(o: str, *digits: int):
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul,
            '**': operator.pow,
            '%': operator.mod,
        }

        if o not in operations.keys():
            raise InvalidOperator

        return functools.reduce(operations[o], digits)

    @staticmethod
    def __convert_number(number: str) -> int:
        if not number.isdigit():
            raise NonNumericalValue

        return int(number)


class MyTestCase(unittest.TestCase):
    def test_it_calculates_prefix_notation(self):
        c = Calculator()
        self.assertEqual(7, c.prefix('+ 3 4'))
        self.assertEqual(12, c.prefix('+ 3 4 5'))
        self.assertEqual(2520, c.prefix('* 3 4 5 6 7'))
        self.assertEqual(5, c.prefix('- 7 2'))
        self.assertEqual(4, c.prefix('/ 8 2'))
        self.assertEqual(9, c.prefix('* 3 3'))
        self.assertEqual(9, c.prefix('** 3 2'))
        self.assertEqual(1, c.prefix('% 7 2'))
        self.assertEqual(7, c.postfix('3 4 +'))
        self.assertEqual(5, c.postfix('7 2 -'))
        self.assertEqual(4, c.postfix('8 2 /'))
        self.assertEqual(9, c.postfix('3 3 *'))
        self.assertEqual(9, c.postfix('3 2 **'))
        self.assertEqual(1, c.postfix('7 2 %'))

    def test_it_raises_an_error_with_invalid_operator(self):
        calculator = Calculator()
        self.assertRaises(InvalidOperator, calculator.prefix, '$ 1 2')

    def test_it_raises_an_error_with_non_numerical_values(self):
        calculator = Calculator()
        self.assertRaises(NonNumericalValue, calculator.prefix, '+ foo 2')
        self.assertRaises(NonNumericalValue, calculator.prefix, '+ 2 bar')


if __name__ == '__main__':
    unittest.main()
