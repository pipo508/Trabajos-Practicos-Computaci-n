import unittest
from nums import Pin


class My_test(unittest.TestCase):
    numbers = Pin()

    def test1(self):
        self.assertEqual(self.numbers.validate_pin("12345"), False)

    def test2(self):
        self.assertEqual(self.numbers.validate_pin("9247"), True)

    def test3(self):
        self.assertEqual(self.numbers.validate_pin("A456"), False)
