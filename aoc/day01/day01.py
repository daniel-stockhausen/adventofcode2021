file_input = 'input/day01.txt'
file_example = 'input/day01-example.txt'


def data_from_file(filename: str) -> list:
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def get_input_data() -> list:
    return data_from_file(file_input)


def get_example_data() -> list:
    return data_from_file(file_example)


def count_increasing_pairs(numbers: list) -> int:
    pairs = list(zip(numbers[:-1], numbers[1:]))
    return count_increasing_generic(pairs)


def count_increasing_triples(numbers: list) -> int:
    triples = list(zip(numbers[:-2], numbers[1:-1], numbers[2:]))
    comparison_pairs = list(zip(triples[:-1], triples[1:]))
    return count_increasing_generic(comparison_pairs)


def count_increasing_generic(pairs_to_compare: list) -> int:
    incr_count = 0
    for current, next in pairs_to_compare:
        if isinstance(current, tuple) and isinstance(next, tuple):
            if sum(current) < sum(next):
                incr_count = incr_count + 1
        else:
            if current < next:
                incr_count = incr_count + 1

    return incr_count


if __name__ == '__main__':
    part1 = count_increasing_pairs(get_input_data())
    print(f"Part 1: {part1}")

    part2 = count_increasing_triples(get_input_data())
    print(f"Part 2: {part2}")
