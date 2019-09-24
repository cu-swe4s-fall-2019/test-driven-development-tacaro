import math_lib
import unittest
import os
import random
import decimal
import statistics

class Test_Math_Lib(unittest.TestCase):
    """A set of unit tests for math_lib"""

    def setUp(self):
        self.direct_compute_array = []
        for i in range(100):
            rand_int = random.randint(1, 100)
            self.direct_compute_array.append(rand_int)

        self.direct_mean_val = statistics.mean(self.direct_compute_array)
        self.direct_std_val = statistics.pstdev(self.direct_compute_array)

    # Tests for list_mean method
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

    def test_mean_rand_ints(self):
        self.assertEqual(math_lib.list_mean(self.direct_list_mean_array),
                                            self.direct_mean_val)

    # Tests for list_stdev method
    def test_stdev_none(self):
        with self.assertRaises(ValueError):
            math_lib.list_stdev(None)

    def test_stdev_empty(self):
        with self.assertRaises(ValueError):
            math_lib.list_stdev([])

    def test_stdev_one_el(self):
        with self.assertRaises(ValueError):
            math_lib.list_stdev([88])

    def test_stdev_only_str(self):
        with self.assertRaises(ValueError):
            math_lib.list_stdev(['a','b','c'])

    def test_stdev_mixed_list(self):
        self.assertEqual(math_lib.list_stdev(['a', 2, 'c', '4']), 1)

    def test_mean_rand_ints(self):
        self.assertAlmostEqual(math_lib.list_stdev(self.direct_compute_array),
                                            self.direct_std_val)

'''
class Test_Get_Data(unittest.TestCase):

    def test_file_nonexistent(self):
        with self.assertRaises(ValueError):
            get_data.read_stdin_col()
'''

if __name__ == '__main__':
    unittest.main()
