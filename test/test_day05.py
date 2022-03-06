import os
import unittest

from aoc.day05.day05 import get_input_data, get_example_data, count_overlapping_coords


class TestDay05(unittest.TestCase):
    def test_05a_example(self):
        self.assertEqual(5, count_overlapping_coords(get_example_data()))

    def test_05a(self):
        self.assertEqual(7380, count_overlapping_coords(get_input_data()))

    def test_05b_example(self):
        self.assertEqual(12, count_overlapping_coords(get_example_data(), use_diagonals=True))

    def test_05b(self):
        self.assertEqual(21373, count_overlapping_coords(get_input_data(), use_diagonals=True))

    def test_05_main(self):
        self.assertEqual(0, os.system("python -m aoc.day05.day05"))
