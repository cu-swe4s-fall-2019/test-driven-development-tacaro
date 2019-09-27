import math_lib
import data_viz
import unittest
import os
import random
import decimal
import statistics
from PIL import Image
import numpy as np


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
            math_lib.list_mean(['a', 'b', 'c'])

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
            math_lib.list_stdev(['a', 'b', 'c'])

    def test_stdev_mixed_list(self):
        self.assertEqual(math_lib.list_stdev(['a', 2, 'c', '4', 'd']), 1)

    def test_mean_rand_ints(self):
        self.assertAlmostEqual(math_lib.list_stdev(self.direct_compute_array),
                               self.direct_std_val)


class Test_Data_Viz(unittest.TestCase):
    """Tests data_viz.py functionality"""

    def setUp(self):
        already = Image.new('RGB', (1, 1))
        already.save('already.png', "PNG")
        data2 = np.array([[1, 3], [5, 9]])
        np.savetxt('data2.txt', data2, delimiter=',')

    def test_boxplot_already_exists(self):
        with self.assertRaises(OSError):
            data_viz.boxplot([1, 2, 3, 4], 'already.png')

    def test_hist_already_exists(self):
        with self.assertRaises(OSError):
            data_viz.histogram([1, 2, 3, 4], 'already.png')

    def test_combo_already_exists(self):
        with self.assertRaises(OSError):
            data_viz.combo([1, 2, 3, 4], 'already.png')

    def test_combo_none_list(self):
        with self.assertRaises(ValueError):
            data_viz.combo(None, 'novel.png')

    def test_combo_empty_list(self):
        with self.assertRaises(ValueError):
            data_viz.combo([], 'novel.png')

    def test_hist_empty_list(self):
        with self.assertRaises(ValueError):
            data_viz.histogram([], 'novel.png')

    def test_hist_none_list(self):
        with self.assertRaises(ValueError):
            data_viz.histogram(None, 'novel.png')

    def test_box_none_list(self):
        with self.assertRaises(ValueError):
            data_viz.boxplot(None, 'novel.png')

    def test_box_empty_list(self):
        with self.assertRaises(ValueError):
            data_viz.boxplot([], 'novel.png')

    def test_box_1d(self):
        with self.assertRaises(TypeError):
            data_viz.boxplot([1, 2, 3], 'novel.png')

    def test_hist_1d(self):
        with self.assertRaises(TypeError):
            data_viz.histogram([1, 2, 3], 'novel.png')

    def test_combo_1d(self):
        with self.assertRaises(TypeError):
            data_viz.combo([1, 2, 3], 'novel.png')


if __name__ == '__main__':
    unittest.main()
