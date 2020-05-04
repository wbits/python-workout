import unittest


def hex_to_int(v: str) -> int:
    result = 0
    for power, val in enumerate(reversed(v)):
        result += int(val, 16) * (16 ** power)

    return result


def hex_to_int_two(v: str) -> int:
    result = 0
    for power, val in enumerate(reversed(v)):
        result += (convert_single_char(val) * (16 ** power))

    return result


def convert_single_char(c: str) -> int:
    result = ord(c)

    if result > 56:
        return result - 87

    return (result - 48)


class TestHexaDecimalOutput(unittest.TestCase):
    def test_hexa_decimal_output(self):
        self.assertEqual(64, hex_to_int('40'))
        self.assertEqual(64, hex_to_int_two('40'))


# print(hex_to_int_two('60'))
# print(hex_to_int_two('c'))
# print(hex_to_int('50'))
# print(hex_to_int_two('50'))
print(hex_to_int('40'))
print(hex_to_int_two('40'))
print(hex_to_int('555'))
print(hex_to_int_two('555'))
print(hex_to_int('1234'))
print(hex_to_int_two('1234'))
# print(hex_to_int('30'))
# print(hex_to_int('20'))
# print(hex_to_int('10'))
