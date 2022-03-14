import os
import unittest

from aoc.day08.day08 import Digit, count_instantly_recognizable_output_digits, decode_line, get_input_data, \
    get_example_data, sum_up_output_values


class TestDay08(unittest.TestCase):
    def test_digit_str(self):
        pattern_cf: str = (
            "      \n"
            "     c\n"
            "     c\n"
            "      \n"
            "     f\n"
            "     f\n"
            "      \n"
        )

        pattern_abcdefg: str = (
            " aaaa \n"
            "b    c\n"
            "b    c\n"
            " dddd \n"
            "e    f\n"
            "e    f\n"
            " gggg \n"
        )

        pattern_abdeg: str = (
            " aaaa \n"
            "b     \n"
            "b     \n"
            " dddd \n"
            "e     \n"
            "e     \n"
            " gggg \n"
        )

        self.assertEqual(pattern_cf, str(Digit("cf")))
        self.assertEqual(pattern_cf, str(Digit("fc")))
        self.assertEqual(pattern_abcdefg, str(Digit("abcdefg")))
        self.assertEqual(pattern_abcdefg, str(Digit("adbcgfe")))
        self.assertEqual(pattern_abdeg, str(Digit("abdeg")))
        with self.assertRaises(ValueError):
            str(Digit("abh"))

    def test_digit_eq(self):
        d1 = Digit("abc")
        d2 = Digit("bcaa")

        self.assertEqual(d1, d2)
        d2.pattern = "ab"
        self.assertNotEqual(d1, d2)
        self.assertNotEqual(d1, "Not a Digit object")

    def test_digit_property_pattern(self):
        d1 = Digit("abc")
        d2 = Digit("de")
        d2.pattern = "bca"

        self.assertEqual(d1, d2)
        self.assertEqual("abc", d2.pattern)
        self.assertTrue(hasattr(d1, "pattern"))

        del d1.pattern
        self.assertFalse(hasattr(d1, "pattern"))

    def test_08a_example(self):
        self.assertEqual(26, count_instantly_recognizable_output_digits(get_example_data()))

    def test_08a(self):
        self.assertEqual(493, count_instantly_recognizable_output_digits(get_input_data()))

    def test_digit_add(self):
        self.assertEqual(Digit("abcdef"), Digit("abc") + Digit("def"))
        self.assertEqual(Digit("abcdef"), Digit("adbc") + Digit("def"))
        self.assertEqual(Digit("abcef"), Digit("cbe") + Digit("efa"))
        self.assertEqual(Digit("aef"), Digit("") + Digit("efa"))
        self.assertEqual(Digit("abf"), Digit("baf") + Digit(""))

    def test_digit_intersect(self):
        self.assertEqual(Digit(""), Digit("abc") & Digit("def"))
        self.assertEqual(Digit("d"), Digit("adbc") & Digit("def"))
        self.assertEqual(Digit("e"), Digit("cbe") & Digit("efa"))
        self.assertEqual(Digit(""), Digit("") & Digit("efa"))
        self.assertEqual(Digit(""), Digit("baf") & Digit(""))

    def test_digit_subtract(self):
        self.assertEqual(Digit("abc"), Digit("abc") - Digit("def"))
        self.assertEqual(Digit("abc"), Digit("adbc") - Digit("def"))
        self.assertEqual(Digit("bc"), Digit("cbe") - Digit("efa"))
        self.assertEqual(Digit(""), Digit("") - Digit("efa"))
        self.assertEqual(Digit("abf"), Digit("baf") - Digit(""))

    def test_decode_line(self):
        self.assertEqual(5353, decode_line(
            ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"],
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
        ))

    def test_08b_example(self):
        self.assertEqual(61229, sum_up_output_values(get_example_data()))

    def test_08b(self):
        self.assertEqual(1010460, sum_up_output_values(get_input_data()))

    def test_08_main(self):
        self.assertEqual(0, os.system("python -m aoc.day08.day08"))
