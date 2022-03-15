import os
import unittest

from aoc.day12.day12 import Connections, NODE_START, build_paths_from, count_valid_paths, get_example_data, \
    get_input_data


class TestDay12(unittest.TestCase):
    def test_get_example_data(self):
        conns: Connections = {
            "start": {"A", "b"},
            "A": {"b", "c", "end"},
            "b": {"A", "d", "end"},
            "c": {"A"},
            "d": {"b"},
            "end": set(),
        }
        self.assertEqual(conns, get_example_data(1))

    def test_build_paths_from(self):
        paths1_expected = [
            "start,A,b,A,c,A,end",
            "start,A,b,A,end",
            "start,A,b,end",
            "start,A,c,A,b,A,end",
            "start,A,c,A,b,end",
            "start,A,c,A,end",
            "start,A,end",
            "start,b,A,c,A,end",
            "start,b,A,end",
            "start,b,end",
        ]
        paths1_actual = build_paths_from(NODE_START, get_example_data(1), set())
        self.assertEqual(sorted(paths1_expected), sorted(paths1_actual))

        paths2_expected = [
            "start,HN,dc,HN,end",
            "start,HN,dc,HN,kj,HN,end",
            "start,HN,dc,end",
            "start,HN,dc,kj,HN,end",
            "start,HN,end",
            "start,HN,kj,HN,dc,HN,end",
            "start,HN,kj,HN,dc,end",
            "start,HN,kj,HN,end",
            "start,HN,kj,dc,HN,end",
            "start,HN,kj,dc,end",
            "start,dc,HN,end",
            "start,dc,HN,kj,HN,end",
            "start,dc,end",
            "start,dc,kj,HN,end",
            "start,kj,HN,dc,HN,end",
            "start,kj,HN,dc,end",
            "start,kj,HN,end",
            "start,kj,dc,HN,end",
            "start,kj,dc,end",
        ]
        paths2_actual = build_paths_from(NODE_START, get_example_data(2), set())
        self.assertEqual(sorted(paths2_expected), sorted(paths2_actual))

    def test_12a_example(self):
        self.assertEqual(10, count_valid_paths(get_example_data(1)))
        self.assertEqual(19, count_valid_paths(get_example_data(2)))
        self.assertEqual(226, count_valid_paths(get_example_data()))

    def test_12a(self):
        self.assertEqual(5212, count_valid_paths(get_input_data()))

    def test_12b_example(self):
        self.assertEqual(36, count_valid_paths(get_example_data(1), allow_single_dupe=True))
        self.assertEqual(103, count_valid_paths(get_example_data(2), allow_single_dupe=True))
        self.assertEqual(3509, count_valid_paths(get_example_data(), allow_single_dupe=True))

    def test_12b(self):
        self.assertEqual(134862, count_valid_paths(get_input_data(), allow_single_dupe=True))

    def test_12_main(self):
        self.assertEqual(0, os.system("python -m aoc.day12.day12"))
