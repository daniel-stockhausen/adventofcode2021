import operator
import re
from collections import defaultdict

day = "day14"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Rules = dict[str, str]
IntByStr = dict[str, int]


def data_from_file(filename: str) -> tuple[str, Rules]:
    with open(filename) as f:
        lines = [line.strip() for line in f]
        polymer = lines[0]

        lines = lines[2:]
        rules: Rules = {}
        for line in lines:
            neighbors, insertion = line.split(" -> ")
            rules[neighbors] = insertion

        return polymer, rules


def get_input_data() -> tuple[str, Rules]:
    return data_from_file(filepath_data)


def get_example_data() -> tuple[str, Rules]:
    return data_from_file(filepath_example)


def insert_once(polymer: str, rules: Rules) -> str:
    polymer_lst = list(polymer)
    for neighbors, insertion in rules.items():
        locations = [m.start() for m in re.finditer(f"(?={neighbors})", polymer)]
        for location in locations:
            polymer_lst[location] += insertion

    return "".join(polymer_lst)


def insert_multi(polymer: str, rules: Rules, n_steps: int) -> str:
    for _ in range(0, n_steps):
        polymer = insert_once(polymer, rules)

    return polymer


def insert_efficiently(count_by_neighbors: IntByStr, count_by_char: IntByStr, rules: Rules, n_steps: int) -> IntByStr:
    for _ in range(0, n_steps):
        for neighbors, count in list(count_by_neighbors.items()):
            insertion = rules[neighbors]
            count_by_char[insertion] += count
            count_by_neighbors[neighbors] -= count
            count_by_neighbors[neighbors[0] + insertion] += count
            count_by_neighbors[insertion + neighbors[1]] += count

    return count_by_char


def subtract_least_common_from_most_common_count(polymer: str, rules: Rules, n_steps: int) -> int:
    polymer = insert_multi(polymer, rules, n_steps)
    count_by_char: IntByStr = {}
    chars = set(polymer)
    for char in chars:
        count_by_char[char] = polymer.count(char)

    count_sorted_by_val = sorted(count_by_char.items(), key=operator.itemgetter(1))
    most_common_count = count_sorted_by_val[-1][1]
    least_common_count = count_sorted_by_val[0][1]
    return most_common_count - least_common_count


def subtract_least_common_from_most_common_count_efficiently(polymer: str, rules: Rules, n_steps: int) -> int:
    count_by_neighbors: IntByStr = defaultdict(int)
    count_by_char: IntByStr = defaultdict(int)
    for i, char in enumerate(polymer[:-1]):
        count_by_neighbors[polymer[i: i + 2]] += 1
        count_by_char[char] += 1
    count_by_char[polymer[-1]] += 1

    count_by_char = insert_efficiently(count_by_neighbors, count_by_char, rules, n_steps)
    count_sorted_by_val = sorted(count_by_char.items(), key=operator.itemgetter(1))
    most_common_count = count_sorted_by_val[-1][1]
    least_common_count = count_sorted_by_val[0][1]
    return most_common_count - least_common_count


if __name__ == "__main__":
    print(day)
    polymer, rules = get_input_data()
    part1 = subtract_least_common_from_most_common_count(polymer, rules, 10)
    print(f"Part 1: {part1}")
    part2 = subtract_least_common_from_most_common_count_efficiently(polymer, rules, 40)
    print(f"Part 2: {part2}")
    print()
