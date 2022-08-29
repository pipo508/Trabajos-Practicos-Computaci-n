import unittest
from nums import consecutivos


class My_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(consecutivos([1, 3, 7, 8], 3, 1), True)

    def test_2(self):
        self.assertEqual(consecutivos([1, 3, 5, 7], 3, 7), False)

    def test_3(self):
        self.assertEqual(consecutivos([1, 6, 9, -3, 4, -78, 0], -3, 4), True)
