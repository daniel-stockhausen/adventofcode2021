from __future__ import annotations
from functools import reduce

day = "day08"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

# segment count for each digit
# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6

# digit count for each segment count
# 2 segments => 1
# 3 segments => 7
# 4 segments => 4
# 5 segments => 2 | 3 | 5
# 6 segments => 0 | 6 | 9
# 7 segments => 8

segments_by_digit: dict[int, str] = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

digit_by_segments: dict[str, int] = {value: key for key, value in segments_by_digit.items()}


class Digit():
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    @property
    def pattern(self) -> str:
        """segments pattern as an ordered string"""
        return self._pattern

    @pattern.setter
    def pattern(self, value: str) -> None:
        self._pattern = "".join(sorted(list(set(value))))

    @pattern.deleter
    def pattern(self) -> None:
        del self._pattern

    def __str__(self) -> str:
        display: list[list[str]] = [list("      ") for _ in range(0, 7)]

        for char in self.pattern:
            match char:
                case "a":
                    display[0] = list(" aaaa ")
                case "b":
                    display[1][0] = "b"
                    display[2][0] = "b"
                case "c":
                    display[1][5] = "c"
                    display[2][5] = "c"
                case "d":
                    display[3] = list(" dddd ")
                case "e":
                    display[4][0] = "e"
                    display[5][0] = "e"
                case "f":
                    display[4][5] = "f"
                    display[5][5] = "f"
                case "g":
                    display[6] = list(" gggg ")
                case _:
                    raise ValueError(f"Segment {char} not supported!")

        display_str = ""
        for line_list in display:
            display_str += "".join(line_list) + "\n"

        return display_str

    def __add__(self, other: Digit) -> Digit:
        return Digit("".join(sorted(list(set(self.pattern) | set(other.pattern)))))

    def __and__(self, other: Digit) -> Digit:
        return Digit("".join(sorted(list(set(self.pattern) & set(other.pattern)))))

    def __sub__(self, other: Digit) -> Digit:
        return Digit("".join(sorted(list(set(self.pattern) - set(other.pattern)))))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Digit):
            return self.pattern == other.pattern
        else:
            return False


def data_from_file(filename: str) -> list[list[list[str]]]:
    with open(filename) as f:
        return [[part.split() for part in line.split(" | ")] for line in f]


def get_input_data() -> list[list[list[str]]]:
    return data_from_file(filepath_data)


def get_example_data() -> list[list[list[str]]]:
    return data_from_file(filepath_example)


def print_digits(digits: list[Digit]) -> None:
    output: list[str] = ["" for _ in range(0, 9)]
    for digit in digits:
        digit_lines = str(digit).split("\n")
        for idx, line in enumerate(digit_lines):
            output[idx] += f"{line}  "

    print("\n".join(output))


def count_instantly_recognizable_output_digits(notes: list[list[list[str]]]) -> int:
    occurence_count = 0
    for _, output_digits in notes:
        occurence_count += sum(1 for digit in output_digits if len(digit) in (2, 3, 4, 7))
    return occurence_count


def translate_segments_pattern(pattern: str, dictionary: dict[str, str]) -> str:
    translation = ""
    for signal in pattern:
        translation += dictionary[signal]

    return translation


def decode_line(signal_patterns: list[str], output_digits: list[str]) -> int:
    digit_obj_by_int: dict[int, Digit] = {}

    signals_by_segment: dict[str, str] = {}
    missing_digits: list[Digit] = []
    for pattern in signal_patterns:
        # signal patterns for 2, 3, 4 and 7 can be easily found out because of their unique segment count
        match len(pattern):
            case 2:
                digit_obj_by_int[1] = Digit(pattern)
            case 3:
                digit_obj_by_int[7] = Digit(pattern)
            case 4:
                digit_obj_by_int[4] = Digit(pattern)
            case 7:
                digit_obj_by_int[8] = Digit(pattern)
            case _:
                missing_digits.append(Digit(pattern))

    # signal for segment g can be found by intersecting all missing patterns 0, 2, 3, 5, 6, 9 and subtracting 7
    digit_segments_a_g = reduce(lambda a, b: a & b, missing_digits)  # all have only segments a and g in common
    # subtracting all segments of digit 7 leaves only segment g remaining
    digit_segment_g = digit_segments_a_g - digit_obj_by_int[7]
    signals_by_segment["g"] = digit_segment_g.pattern

    digit_segment_a = digit_segments_a_g - digit_segment_g
    signals_by_segment["a"] = digit_segment_a.pattern

    # digit 4 - 1 results in a digit with segments b and d
    digit_segments_b_d = digit_obj_by_int[4] - digit_obj_by_int[1]

    # digit 8 - 7 - bd results in a digit with segments e and g
    digit_segments_e_g = (digit_obj_by_int[8] - digit_obj_by_int[7]) - digit_segments_b_d
    digit_segment_e = digit_segments_e_g - digit_segment_g
    signals_by_segment["e"] = digit_segment_e.pattern

    # the whole group of the 3 patterns for 2, 3, 5 can be easily found with their unique segment count of 5
    # intersecting digits 2, 3, 5 will result in a digit with segments a, d, g - providing a way to get to d
    digits_with_pattern_length_5: list[Digit] = []
    for digit in missing_digits:
        if len(digit.pattern) == 5:
            digits_with_pattern_length_5.append(digit)
    digit_segments_a_d_g = reduce(lambda a, b: a & b, digits_with_pattern_length_5)

    digit_segment_d = digit_segments_a_d_g - digit_segments_a_g
    signals_by_segment["d"] = digit_segment_d.pattern

    digit_segment_b = digit_segments_b_d - digit_segment_d
    signals_by_segment["b"] = digit_segment_b.pattern

    # the whole group of the 3 patterns for 0, 6, 9 can be easily found with their unique segment count of 6
    # intersecting digits 0, 6, 9 will result in a digit with segments a, b, f, g - providing a way to get to f
    digits_with_pattern_length_6: list[Digit] = []
    for digit in missing_digits:
        if len(digit.pattern) == 6:
            digits_with_pattern_length_6.append(digit)
    digit_segments_a_b_f_g = reduce(lambda a, b: a & b, digits_with_pattern_length_6)

    digit_segment_f = (digit_segments_a_b_f_g - digit_segments_a_g) - digit_segment_b
    signals_by_segment["f"] = digit_segment_f.pattern

    # digit 1 - f results in last missing segment c
    digit_segment_c = digit_obj_by_int[1] - digit_segment_f
    signals_by_segment["c"] = digit_segment_c.pattern

    segments_by_signals = {value: key for key, value in signals_by_segment.items()}

    output = ""
    for digit_pattern in output_digits:
        sorted_translation = "".join(sorted(translate_segments_pattern(digit_pattern, segments_by_signals)))
        output += str(digit_by_segments[sorted_translation])

    return int(output)


def sum_up_output_values(notes: list[list[list[str]]]) -> int:
    return sum(decode_line(line[0], line[1]) for line in notes)


if __name__ == "__main__":
    print(day)
    print()
    print("### KNOWN DIGITS ###\n")
    known_ints = [1, 4, 7, 8]
    known_digits: dict[int, Digit] = {}
    for number in known_ints:
        digit = Digit(segments_by_digit[number])
        known_digits[number] = digit
    print_digits(list(known_digits.values()))

    print("### MISSING DIGITS ###\n")
    wanted_ints = [0, 2, 3, 5, 6, 9]
    wanted_digits: dict[int, Digit] = {}
    for number in wanted_ints:
        digit = Digit(segments_by_digit[number])
        wanted_digits[number] = digit
    print_digits(list(wanted_digits.values()))

    print("### EXPERIMENTAL DIGITS ###\n")
    # see decode_line() for explanation on how we got to the following lines
    tmp_digits: dict[str, Digit] = {}
    tmp_digits["ag"] = reduce(lambda a, b: a & b, wanted_digits.values())
    tmp_digits["g"] = tmp_digits["ag"] - known_digits[7]
    tmp_digits["a"] = tmp_digits["ag"] - tmp_digits["g"]
    tmp_digits["bd"] = known_digits[4] - known_digits[1]
    tmp_digits["eg"] = (known_digits[8] - known_digits[7]) - tmp_digits["bd"]
    tmp_digits["e"] = tmp_digits["eg"] - tmp_digits["g"]
    tmp_digits["adg"] = reduce(lambda a, b: a & b, [wanted_digits[2], wanted_digits[3], wanted_digits[5]])
    tmp_digits["d"] = tmp_digits["adg"] - tmp_digits["ag"]
    tmp_digits["b"] = tmp_digits["bd"] - tmp_digits["d"]
    tmp_digits["abfg"] = reduce(lambda a, b: a & b, [wanted_digits[0], wanted_digits[6], wanted_digits[9]])
    tmp_digits["f"] = (tmp_digits["abfg"] - tmp_digits["ag"]) - tmp_digits["b"]
    tmp_digits["c"] = known_digits[1] - tmp_digits["f"]
    print_digits(list(tmp_digits.values()))

    part1 = count_instantly_recognizable_output_digits(get_input_data())
    print(f"Part 1: {part1}")
    part2 = sum_up_output_values(get_input_data())
    print(f"Part 2: {part2}")
    print()
