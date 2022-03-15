import os
import unittest

from aoc.day13.day13 import count_dots_after_folds, do_fold, do_folds, get_example_data, get_input_data


def paper_str_to_lst(paper_str: str) -> list[list[str]]:
    paper_expected1: list[list[str]] = []
    for line in paper_str.split("\n"):
        paper_expected1.append(list(line))
    return paper_expected1


class TestDay13(unittest.TestCase):
    def test_get_example_data(self):
        paper_expected_str = (
            "...#..#..#.\n"
            "....#......\n"
            "...........\n"
            "#..........\n"
            "...#....#.#\n"
            "...........\n"
            "...........\n"
            "...........\n"
            "...........\n"
            "...........\n"
            ".#....#.##.\n"
            "....#......\n"
            "......#...#\n"
            "#..........\n"
            "#.#........"
        )
        paper_expected = paper_str_to_lst(paper_expected_str)

        paper_actual, folds_actual = get_example_data()
        self.assertEqual(paper_expected, paper_actual)
        self.assertEqual([("y", 7), ("x", 5)], folds_actual)

    def test_do_fold(self):
        paper_expected1_str = (
            "#.##..#..#.\n"
            "#...#......\n"
            "......#...#\n"
            "#...#......\n"
            ".#.#..#.###\n"
            "...........\n"
            "..........."
        )
        paper_expected1 = paper_str_to_lst(paper_expected1_str)

        paper, folds = get_example_data()
        paper_folded1 = do_fold(paper, folds[0])
        self.assertEqual(paper_expected1, paper_folded1)

        paper_expected2_str = (
            "#####\n"
            "#...#\n"
            "#...#\n"
            "#...#\n"
            "#####\n"
            ".....\n"
            "....."
        )
        paper_expected2 = paper_str_to_lst(paper_expected2_str)

        paper_folded2 = do_fold(paper_folded1, folds[1])
        self.assertEqual(paper_expected2, paper_folded2)

    def test_13a_example(self):
        paper, folds = get_example_data()
        paper_folded1 = count_dots_after_folds(paper, folds, 1)
        self.assertEqual(17, paper_folded1)

    def test_13a(self):
        paper, folds = get_input_data()
        self.assertEqual(814, count_dots_after_folds(paper, folds, 1))

    def test_13b(self):
        paper_expected_str = (
            "###..####.####.#..#.###...##..####.###..\n"
            "#..#....#.#....#..#.#..#.#..#.#....#..#.\n"
            "#..#...#..###..####.#..#.#..#.###..#..#.\n"
            "###...#...#....#..#.###..####.#....###..\n"
            "#....#....#....#..#.#.#..#..#.#....#.#..\n"
            "#....####.####.#..#.#..#.#..#.####.#..#."
        )  # PZEHRAER
        paper_expected = paper_str_to_lst(paper_expected_str)

        paper, folds = get_input_data()
        self.assertEqual(paper_expected, do_folds(paper, folds))

    def test_13_main(self):
        self.assertEqual(0, os.system("python -m aoc.day13.day13"))
