import numpy as np

day = 'day07'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> list[int]:
    with open(filename) as f:
        crabs_line = f.readline().strip()
        crabs: list[int] = [int(x) for x in crabs_line.split(',')]
    return crabs


def get_input_data() -> list[int]:
    return data_from_file(filepath_data)


def get_example_data() -> list[int]:
    return data_from_file(filepath_example)


def gauss_sum(n: int) -> int:
    if n < 0:
        raise ValueError("Negative input numbers are not allowed")
    return int((n * (n + 1)) / 2)


def calc_fuel(crabs: list[int], target: int, increasing_cost: bool = False) -> int:
    fuel_cost = 0
    for crab in crabs:
        distance = max(crab, target) - min(crab, target)
        if not increasing_cost:
            fuel_cost += distance
        else:
            fuel_cost += gauss_sum(distance)

    return fuel_cost


def calc_fuel_for_cheapest_target(crabs: list[int], increasing_cost: bool = False) -> int:
    if not increasing_cost:
        return calc_fuel(crabs, int(np.median(crabs)), increasing_cost)
    else:
        lowest = calc_fuel(crabs, max(crabs), increasing_cost=True)
        for n in range(min(crabs), max(crabs)):
            current = calc_fuel(crabs, n, increasing_cost=True)
            if lowest > current:
                lowest = current
        return lowest


if __name__ == '__main__':
    print(day)
    part1 = calc_fuel_for_cheapest_target(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_fuel_for_cheapest_target(get_input_data(), increasing_cost=True)
    print(f"Part 2: {part2}")
    print()
