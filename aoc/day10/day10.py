day = "day10"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

opening_token_by_closing_token: dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

closing_token_by_opening_token: dict[str, str] = {value: key for key, value in opening_token_by_closing_token.items()}


def data_from_file(filename: str) -> list[str]:
    with open(filename) as f:
        lines = [line.strip() for line in f]
    return lines


def get_input_data() -> list[str]:
    return data_from_file(filepath_data)


def get_example_data() -> list[str]:
    return data_from_file(filepath_example)


def score_line_error(line: str) -> int:
    error_score_by_token: dict[str, int] = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    stack: list[str] = []
    for token in line:
        if token in opening_token_by_closing_token.values():
            stack.append(token)
        elif token in closing_token_by_opening_token.values():
            opening_token_expected = opening_token_by_closing_token[token]
            opening_token_actual = stack.pop()
            if opening_token_actual != opening_token_expected:
                return error_score_by_token[token]
        else:
            raise ValueError(f"Unsupported token '{token}'")

    return 0


def calc_file_error_score(lines: list[str]) -> int:
    return sum(score_line_error(line) for line in lines)


def calc_missing_tokens_for_incomplete_line(line: str) -> str:
    missing_tokens = ""

    stack: list[str] = []
    for token in line:
        if token in opening_token_by_closing_token.values():
            stack.append(token)
        else:
            stack.pop()

    while len(stack) > 0:
        token = stack.pop()
        if token in opening_token_by_closing_token.values():
            missing_tokens += closing_token_by_opening_token[token]
        else:
            stack.pop()

    return missing_tokens


def score_line_completion(line: str) -> int:
    error_score_by_token: dict[str, int] = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    missing_tokens = calc_missing_tokens_for_incomplete_line(line)

    error_score = 0
    for token in missing_tokens:
        error_score = error_score * 5 + error_score_by_token[token]

    return error_score


def calc_completion_string_middle_score(lines: list[str]) -> int:
    incomplete_lines: list[str] = []
    for line in lines:
        if score_line_error(line) == 0:
            incomplete_lines.append(line)

    scores: list[int] = []
    for line in incomplete_lines:
        scores.append(score_line_completion(line))

    scores_sorted = sorted(scores)
    middle_index = int((len(scores_sorted) - 1) / 2)
    return scores_sorted[middle_index]


if __name__ == "__main__":
    print(day)
    part1 = calc_file_error_score(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_completion_string_middle_score(get_input_data())
    print(f"Part 2: {part2}")
    print()
