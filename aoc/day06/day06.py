day = 'day06'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> list[int]:
    with open(filename) as f:
        lanternfish_line = f.readline().strip()
        lanternfish: list[int] = [int(x) for x in lanternfish_line.split(',')]
    return lanternfish


def get_input_data() -> list[int]:
    return data_from_file(filepath_data)


def get_example_data() -> list[int]:
    return data_from_file(filepath_example)


def elapse_day(lanternfish: list[int]) -> list[int]:
    additional_fish: list[int] = []

    for i, fish in enumerate(lanternfish):
        if fish == 0:
            lanternfish[i] = 6
            additional_fish.append(8)
        else:
            lanternfish[i] -= 1

    lanternfish.extend(additional_fish)
    return lanternfish


def init_efficiency_mode(lanternfish: list[int]) -> dict[int, int]:
    fish_count_by_age = {n: 0 for n in range(0, 9)}

    for fish in lanternfish:
        fish_count_by_age[fish] += 1

    return fish_count_by_age


def elapse_day_efficiently(fish_count_by_age: dict[int, int]) -> dict[int, int]:
    fish_count_by_age_next_day: dict[int, int] = {}

    for n in range(0, 9):
        fish_count_by_age_next_day[n] = fish_count_by_age[(n + 1) % 9]
    fish_count_by_age_next_day[6] += fish_count_by_age[0]

    return fish_count_by_age_next_day


def elapse_days(lanternfish: list[int], days: int, efficiently: bool = False) -> int:
    if not efficiently:
        for _ in range(0, days):
            lanternfish = elapse_day(lanternfish)
        return len(lanternfish)
    else:
        lanternfish_dict: dict[int, int] = init_efficiency_mode(lanternfish)
        for _ in range(0, days):
            lanternfish_dict = elapse_day_efficiently(lanternfish_dict)
        return sum(x for x in lanternfish_dict.values())


if __name__ == '__main__':
    print(day)
    part1 = elapse_days(get_input_data(), 80)
    print(f"Part 1: {part1}")
    part2 = elapse_days(get_input_data(), 256, efficiently=True)
    print(f"Part 2: {part2}")
    print()
