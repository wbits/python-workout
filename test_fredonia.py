import unittest
from fredonia import calculate_tax


class FredoniaTestCase(unittest.TestCase):
    def test_it_calculates_tax(self):
        self.assertEqual(625, calculate_tax(500, 'Harpo', 12))
