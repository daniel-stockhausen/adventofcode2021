import os
import unittest

from aoc.day06.day06 import elapse_days, get_example_data, get_input_data


class TestDay06(unittest.TestCase):
    def test_06a_example(self):
        self.assertEqual(26, elapse_days(get_example_data(), 18))
        self.assertEqual(5934, elapse_days(get_example_data(), 80))

    def test_06a(self):
        self.assertEqual(343441, elapse_days(get_input_data(), 80))

    def test_06b_example(self):
        self.assertEqual(26, elapse_days(get_example_data(), 18, efficiently=True))
        self.assertEqual(5934, elapse_days(get_example_data(), 80, efficiently=True))
        self.assertEqual(26984457539, elapse_days(get_example_data(), 256, efficiently=True))

    def test_06b(self):
        self.assertEqual(343441, elapse_days(get_input_data(), 80, efficiently=True))
        self.assertEqual(1569108373832, elapse_days(get_input_data(), 256, efficiently=True))

    def test_06_main(self):
        self.assertEqual(0, os.system("python -m aoc.day06.day06"))
