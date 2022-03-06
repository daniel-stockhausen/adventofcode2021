import os
import unittest

from aoc.day04.day04 import get_input_data, get_example_data, calc_score_of_winning_board


class TestDay04(unittest.TestCase):
    def test_04a_example(self):
        draw_numbers, boards = get_example_data()
        self.assertEqual(4512, calc_score_of_winning_board(draw_numbers, boards))

    def test_04a(self):
        draw_numbers, boards = get_input_data()
        self.assertEqual(58412, calc_score_of_winning_board(draw_numbers, boards))

    def test_04b_example(self):
        draw_numbers, boards = get_example_data()
        self.assertEqual(1924, calc_score_of_winning_board(draw_numbers, boards, True))

    def test_04b(self):
        draw_numbers, boards = get_input_data()
        self.assertEqual(10030, calc_score_of_winning_board(draw_numbers, boards, True))

    def test_04_main(self):
        self.assertEqual(0, os.system("python -m aoc.day04.day04"))
