import os
import unittest

from aoc.day03.day03 import calc_co2_scrubber_rating, calc_life_support_rating, calc_oxygen_generator_rating, \
    calc_power_consumption, get_example_data, get_input_data


class TestDay03(unittest.TestCase):
    def test_03a_example(self):
        self.assertEqual(198, calc_power_consumption(get_example_data()))

    def test_03a(self):
        self.assertEqual(1082324, calc_power_consumption(get_input_data()))

    def test_03b_calc_oxygen_generator_rating_example(self):
        self.assertEqual(23, calc_oxygen_generator_rating(get_example_data()))

    def test_03b_calc_co2_scrubber_rating_example(self):
        self.assertEqual(10, calc_co2_scrubber_rating(get_example_data()))

    def test_03b_example(self):
        self.assertEqual(230, calc_life_support_rating(get_example_data()))

    def test_03b(self):
        self.assertEqual(1353024, calc_life_support_rating(get_input_data()))

    def test_03_main(self):
        self.assertEqual(0, os.system("python -m aoc.day03.day03"))
