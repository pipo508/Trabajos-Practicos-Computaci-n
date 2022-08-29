import unittest
from sum import Sum


class My_test(unittest.TestCase):
    numbers = Sum()

    def test1(self):
        self.assertEqual(self.numbers.sum_numbers([7, 6, 5]), 2)