import os
import unittest

from aoc.day09.day09 import aggregate_basin_coords, get_input_data, get_example_data, is_low_point, \
    multiply_three_largest_basins_size, sum_risk_levels_of_low_points


class TestDay09(unittest.TestCase):
    def test_is_low_point(self):
        self.assertTrue(is_low_point(0, 1, get_example_data()))
        self.assertTrue(is_low_point(0, 9, get_example_data()))
        self.assertTrue(is_low_point(2, 2, get_example_data()))
        self.assertTrue(is_low_point(4, 6, get_example_data()))

    def test_09a_example(self):
        self.assertEqual(15, sum_risk_levels_of_low_points(get_example_data()))

    def test_09a(self):
        self.assertEqual(522, sum_risk_levels_of_low_points(get_input_data()))

    def test_calc_basin_locations_from_point(self):
        self.assertEqual([(0, 0), (0, 1), (1, 0)], aggregate_basin_coords(0, 0, get_example_data()))
        self.assertEqual([(0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 6), (1, 8), (1, 9), (2, 9)],
                         aggregate_basin_coords(0, 9, get_example_data()))
        self.assertEqual([(1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 1),
                          (3, 2), (3, 3), (3, 4), (4, 1)], aggregate_basin_coords(2, 2, get_example_data()))
        self.assertEqual([(2, 7), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9)],
                         aggregate_basin_coords(4, 6, get_example_data()))

    def test_09b_example(self):
        self.assertEqual(1134, multiply_three_largest_basins_size(get_example_data()))

    def test_09b(self):
        self.assertEqual(916688, multiply_three_largest_basins_size(get_input_data()))

    def test_09_main(self):
        self.assertEqual(0, os.system("python -m aoc.day09.day09"))
