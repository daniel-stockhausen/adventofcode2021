import os
import unittest

from aoc.day15.day15 import calc_lowest_route_risk, get_example_data, get_input_data, tile_riskmap


class TestDay15(unittest.TestCase):
    def test_15a_example(self):
        self.assertEqual(40, calc_lowest_route_risk(get_example_data()))

    def test_15a(self):
        self.assertEqual(755, calc_lowest_route_risk(get_input_data()))

    def test_tile_riskmap(self):
        riskmap = get_example_data()

        riskmap_times1_actual = tile_riskmap(riskmap, 1)
        self.assertEqual(riskmap, riskmap_times1_actual)

        riskmap_times2_expected = [
            [1, 1, 6, 3, 7, 5, 1, 7, 4, 2, 2, 2, 7, 4, 8, 6, 2, 8, 5, 3],
            [1, 3, 8, 1, 3, 7, 3, 6, 7, 2, 2, 4, 9, 2, 4, 8, 4, 7, 8, 3],
            [2, 1, 3, 6, 5, 1, 1, 3, 2, 8, 3, 2, 4, 7, 6, 2, 2, 4, 3, 9],
            [3, 6, 9, 4, 9, 3, 1, 5, 6, 9, 4, 7, 1, 5, 1, 4, 2, 6, 7, 1],
            [7, 4, 6, 3, 4, 1, 7, 1, 1, 1, 8, 5, 7, 4, 5, 2, 8, 2, 2, 2],
            [1, 3, 1, 9, 1, 2, 8, 1, 3, 7, 2, 4, 2, 1, 2, 3, 9, 2, 4, 8],
            [1, 3, 5, 9, 9, 1, 2, 4, 2, 1, 2, 4, 6, 1, 1, 2, 3, 5, 3, 2],
            [3, 1, 2, 5, 4, 2, 1, 6, 3, 9, 4, 2, 3, 6, 5, 3, 2, 7, 4, 1],
            [1, 2, 9, 3, 1, 3, 8, 5, 2, 1, 2, 3, 1, 4, 2, 4, 9, 6, 3, 2],
            [2, 3, 1, 1, 9, 4, 4, 5, 8, 1, 3, 4, 2, 2, 1, 5, 5, 6, 9, 2],
            [2, 2, 7, 4, 8, 6, 2, 8, 5, 3, 3, 3, 8, 5, 9, 7, 3, 9, 6, 4],
            [2, 4, 9, 2, 4, 8, 4, 7, 8, 3, 3, 5, 1, 3, 5, 9, 5, 8, 9, 4],
            [3, 2, 4, 7, 6, 2, 2, 4, 3, 9, 4, 3, 5, 8, 7, 3, 3, 5, 4, 1],
            [4, 7, 1, 5, 1, 4, 2, 6, 7, 1, 5, 8, 2, 6, 2, 5, 3, 7, 8, 2],
            [8, 5, 7, 4, 5, 2, 8, 2, 2, 2, 9, 6, 8, 5, 6, 3, 9, 3, 3, 3],
            [2, 4, 2, 1, 2, 3, 9, 2, 4, 8, 3, 5, 3, 2, 3, 4, 1, 3, 5, 9],
            [2, 4, 6, 1, 1, 2, 3, 5, 3, 2, 3, 5, 7, 2, 2, 3, 4, 6, 4, 3],
            [4, 2, 3, 6, 5, 3, 2, 7, 4, 1, 5, 3, 4, 7, 6, 4, 3, 8, 5, 2],
            [2, 3, 1, 4, 2, 4, 9, 6, 3, 2, 3, 4, 2, 5, 3, 5, 1, 7, 4, 3],
            [3, 4, 2, 2, 1, 5, 5, 6, 9, 2, 4, 5, 3, 3, 2, 6, 6, 7, 1, 3],
        ]
        riskmap_times2_actual = tile_riskmap(riskmap, 2)
        self.assertEqual(riskmap_times2_expected, riskmap_times2_actual)

        riskmap_times5_expected = get_example_data(2)
        riskmap_times5_actual = tile_riskmap(riskmap, 5)
        self.assertEqual(riskmap_times5_expected, riskmap_times5_actual)

    def test_15b_example(self):
        self.assertEqual(315, calc_lowest_route_risk(tile_riskmap(get_example_data(), 5)))

    def test_15b(self):
        self.assertEqual(3016, calc_lowest_route_risk(tile_riskmap(get_input_data(), 5)))

    def test_15_main(self):
        self.assertEqual(0, os.system("python -m aoc.day15.day15"))
