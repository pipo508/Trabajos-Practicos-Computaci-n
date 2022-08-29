import unittest
from nums import Nums


class My_test(unittest.TestCase):
    numers = Nums()
    def test(self):
        nums = list(range(0, 101))
        self.numers.remove_number(nums,5)
        self.test.assert_equals(self.numers.missing_number(nums), 5)

"""
 def test_1(self):
        def test_1(self):
            nums = list(range(0, 101))
            self.numers.remove_number(nums, 5)
            self.assert_equals(self.numers.missing_number(nums), 5)
"""