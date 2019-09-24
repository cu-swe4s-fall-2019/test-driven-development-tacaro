import math_lib.py
import unittest
import os
import random
import statistics

class Test_Math_Lib(unittest.TestCase):
    """A set of unit tests for math_lib"""

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            math_lib.list_mean([])

    def test_mean_none(self):
        with self.assertRaises(ValueError):
            math_lib.list_mean(None)

    def test_mean_only_str(self):
        with self.assertRaises(ValueError):
            math_lib.list_mean(['a','b','c'])

    def test_mean_mixed_list(self):
        self.assertEqual(math_lib.list_mean(['a', 2, 'c', '4']), 3)
