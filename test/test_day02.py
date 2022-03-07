import os
import unittest

from aoc.day02.day02 import get_input_data, get_example_data, calculate_destination, calculate_destination_part2


class TestDay02(unittest.TestCase):
    def test_calculate_destination_unsupported_cmd(self):
        self.assertEqual(0, calculate_destination([("xyz", 5)]))

    def test_02a_example(self):
        self.assertEqual(150, calculate_destination(get_example_data()))

    def test_02a(self):
        self.assertEqual(2120749, calculate_destination(get_input_data()))

    def test_calculate_destination_part2_unsupported_cmd(self):
        self.assertEqual(0, calculate_destination_part2([("xyz", 5)]))

    def test_02b_example(self):
        self.assertEqual(900, calculate_destination_part2(get_example_data()))

    def test_02b(self):
        self.assertEqual(2138382217, calculate_destination_part2(get_input_data()))

    def test_02_main(self):
        self.assertEqual(0, os.system("python -m aoc.day02.day02"))
