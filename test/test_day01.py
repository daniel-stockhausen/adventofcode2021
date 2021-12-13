import os
import unittest

from aoc.day01.day01 import count_increasing_pairs, count_increasing_triples, get_input_data, get_example_data


class TestDay01(unittest.TestCase):
    def test_01a_example(self):
        self.assertEqual(7, count_increasing_pairs(get_example_data()))

    def test_01a(self):
        self.assertEqual(1167, count_increasing_pairs(get_input_data()))

    def test_01b_example(self):
        self.assertEqual(5, count_increasing_triples(get_example_data()))

    def test_01b(self):
        self.assertEqual(1130, count_increasing_triples(get_input_data()))

    def test_01_main(self):
        self.assertEqual(0, os.system("python -m aoc.day01.day01"))
