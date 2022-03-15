import os
import unittest

from aoc.day11.day11 import OctopusLevels, calc_synchronized_step, count_flashes_for_steps, get_example_data, \
    get_input_data, process_step_count_flashes


class TestDay11(unittest.TestCase):
    map_str_00 = (
        "11111\n"
        "19991\n"
        "19191\n"
        "19991\n"
        "11111"
    )

    map_str_01 = (
        "34543\n"
        "40004\n"
        "50005\n"
        "40004\n"
        "34543"
    )

    map_str_example = (
        "5483143223\n"
        "2745854711\n"
        "5264556173\n"
        "6141336146\n"
        "6357385478\n"
        "4167524645\n"
        "2176841721\n"
        "6882881134\n"
        "4846848554\n"
        "5283751526"
    )

    def test_octopus_map_property_map(self):
        lvls1 = OctopusLevels(self.map_str_00)
        self.assertEqual([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1]
        ], lvls1.map)

        lvls_example_1 = OctopusLevels(self.map_str_example)
        lvls_example_2 = get_example_data()
        self.assertEqual(lvls_example_1, lvls_example_2)

    def test_octopus_map_repr(self):
        lvls = OctopusLevels(self.map_str_00)
        self.assertEqual(self.map_str_00, str(lvls))

    def test_octopus_map_eq(self):
        lvls1 = OctopusLevels(self.map_str_00)
        lvls2 = OctopusLevels(self.map_str_00)
        self.assertEqual(lvls1, lvls2)

        lvls2.map = self.map_str_01
        self.assertNotEqual(lvls1, lvls2)

        lvls2.map = self.map_str_00
        self.assertEqual(lvls2, lvls1)

        self.assertNotEqual(lvls1, lvls2.map)

    def test_process_step(self):
        lvls = OctopusLevels(self.map_str_00)
        process_step_count_flashes(lvls)

        self.assertNotEqual(OctopusLevels(self.map_str_00), lvls)
        self.assertEqual(OctopusLevels(self.map_str_01), lvls)

    def test_count_flashes_for_steps(self):
        self.assertEqual(9, count_flashes_for_steps(1, OctopusLevels(self.map_str_00)))
        self.assertEqual(9, count_flashes_for_steps(2, OctopusLevels(self.map_str_00)))
        self.assertEqual(9, count_flashes_for_steps(3, OctopusLevels(self.map_str_00)))
        self.assertEqual(9, count_flashes_for_steps(4, OctopusLevels(self.map_str_00)))
        self.assertEqual(9, count_flashes_for_steps(5, OctopusLevels(self.map_str_00)))

    def test_11a_example(self):
        self.assertEqual(1656, count_flashes_for_steps(100, get_example_data()))

    def test_11a(self):
        self.assertEqual(1735, count_flashes_for_steps(100, get_input_data()))

    def test_11b_example(self):
        self.assertEqual(195, calc_synchronized_step(get_example_data()))

    def test_11b(self):
        self.assertEqual(400, calc_synchronized_step(get_input_data()))

    def test_11_main(self):
        self.assertEqual(0, os.system("python -m aoc.day11.day11"))
