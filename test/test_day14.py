import os
import unittest

from aoc.day14.day14 import get_example_data, get_input_data, insert_multi, \
    subtract_least_common_from_most_common_count, subtract_least_common_from_most_common_count_efficiently


class TestDay14(unittest.TestCase):
    def test_insert_multi(self):
        polymer, rules = get_example_data()
        self.assertEqual("NCNBCHB", insert_multi(polymer, rules, 1))
        self.assertEqual("NBCCNBBBCBHCB", insert_multi(polymer, rules, 2))
        self.assertEqual("NBBBCNCCNBBNBNBBCHBHHBCHB", insert_multi(polymer, rules, 3))
        self.assertEqual("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB", insert_multi(polymer, rules, 4))

    def test_14a_example(self):
        polymer, rules = get_example_data()
        paper_folded = subtract_least_common_from_most_common_count(polymer, rules, 10)
        self.assertEqual(1588, paper_folded)

    def test_14a(self):
        polymer, rules = get_input_data()
        paper_folded = subtract_least_common_from_most_common_count(polymer, rules, 10)
        self.assertEqual(2408, paper_folded)

    def test_14b_example(self):
        polymer, rules = get_example_data()
        paper_folded = subtract_least_common_from_most_common_count_efficiently(polymer, rules, 40)
        self.assertEqual(2188189693529, paper_folded)

    def test_14b(self):
        polymer, rules = get_input_data()
        paper_folded = subtract_least_common_from_most_common_count_efficiently(polymer, rules, 40)
        self.assertEqual(2651311098752, paper_folded)

    def test_14_main(self):
        self.assertEqual(0, os.system("python -m aoc.day14.day14"))
