import os
import unittest

from aoc.day10.day10 import calc_completion_string_middle_score, score_line_error, calc_file_error_score, \
    calc_missing_tokens_for_incomplete_line, get_input_data, get_example_data, score_line_completion


class TestDay10(unittest.TestCase):
    def test_score_line_error(self):
        self.assertEqual(0, score_line_error("([])"))
        self.assertEqual(0, score_line_error("{()()()}"))
        self.assertEqual(0, score_line_error("<([{}])>"))
        self.assertEqual(0, score_line_error("[<>({}){}[([])<>]]"))
        self.assertEqual(0, score_line_error("(((((((((())))))))))"))

        self.assertEqual(1197, score_line_error("{([(<{}[<>[]}>{[]{[(<()>"))
        self.assertEqual(3, score_line_error("[[<[([]))<([[{}[[()]]]"))
        self.assertEqual(57, score_line_error("[{[{({}]{}}([{[{{{}}([]"))
        self.assertEqual(3, score_line_error("[<(<(<(<{}))><([]([]()"))
        self.assertEqual(25137, score_line_error("<{([([[(<>()){}]>(<<{{"))

    def test_10a_example(self):
        self.assertEqual(26397, calc_file_error_score(get_example_data()))

    def test_10a(self):
        self.assertEqual(394647, calc_file_error_score(get_input_data()))

    def test_calc_missing_tokens_for_incomplete_line(self):
        self.assertEqual("}}]])})]",
                         calc_missing_tokens_for_incomplete_line("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(")}>]})",
                         calc_missing_tokens_for_incomplete_line("[(()[<>])]({[<{<<[]>>("))
        self.assertEqual("}}>}>))))",
                         calc_missing_tokens_for_incomplete_line("(((({<>}<{<{<>}{[]{[]{}"))
        self.assertEqual("]]}}]}]}>",
                         calc_missing_tokens_for_incomplete_line("{<[[]]>}<{[{[{[]{()[[[]"))
        self.assertEqual("])}>",
                         calc_missing_tokens_for_incomplete_line("<{([{{}}[<[[[<>{}]]]>[]]"))

    def test_score_line_completion(self):
        self.assertEqual(288957, score_line_completion("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(5566, score_line_completion("[(()[<>])]({[<{<<[]>>("))
        self.assertEqual(1480781, score_line_completion("(((({<>}<{<{<>}{[]{[]{}"))
        self.assertEqual(995444, score_line_completion("{<[[]]>}<{[{[{[]{()[[[]"))
        self.assertEqual(294, score_line_completion("<{([{{}}[<[[[<>{}]]]>[]]"))

    def test_10b_example(self):
        self.assertEqual(288957, calc_completion_string_middle_score(get_example_data()))

    def test_10b(self):
        self.assertEqual(2380061249, calc_completion_string_middle_score(get_input_data()))

    def test_10_main(self):
        self.assertEqual(0, os.system("python -m aoc.day10.day10"))
