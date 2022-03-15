import os
import unittest

from aoc.day07.day07 import calc_fuel, calc_fuel_for_cheapest_target, gauss_sum, get_example_data, get_input_data


class TestDay07(unittest.TestCase):
    def test_07a_calc_fuel_example(self):
        self.assertEqual(37, calc_fuel(get_example_data(), 2))
        self.assertEqual(41, calc_fuel(get_example_data(), 1))
        self.assertEqual(39, calc_fuel(get_example_data(), 3))
        self.assertEqual(71, calc_fuel(get_example_data(), 10))

    def test_07a_example(self):
        self.assertEqual(37, calc_fuel_for_cheapest_target(get_example_data()))

    def test_07a(self):
        self.assertEqual(340056, calc_fuel_for_cheapest_target(get_input_data()))

    def test_07b_gauss_sum(self):
        with self.assertRaises(ValueError):
            gauss_sum(-1)
        self.assertEqual(0, gauss_sum(0))
        self.assertEqual(1, gauss_sum(1))
        self.assertEqual(6, gauss_sum(3))
        self.assertEqual(15, gauss_sum(5))
        self.assertEqual(21, gauss_sum(6))

    def test_07b_calc_fuel_example(self):
        self.assertEqual(168, calc_fuel(get_example_data(), 5, increasing_cost=True))
        self.assertEqual(206, calc_fuel(get_example_data(), 2, increasing_cost=True))

    def test_07b_example(self):
        self.assertEqual(168, calc_fuel_for_cheapest_target(get_example_data(), increasing_cost=True))

    def test_07b(self):
        self.assertEqual(96592275, calc_fuel_for_cheapest_target(get_input_data(), increasing_cost=True))

    def test_07_main(self):
        self.assertEqual(0, os.system("python -m aoc.day07.day07"))
