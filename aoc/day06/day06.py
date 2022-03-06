day = 'day06'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> dict:
    with open(filename) as f:
        lanternfish_line = f.readline().strip()
        lanternfish = [int(x) for x in lanternfish_line.split(',')]
    return lanternfish


def get_input_data() -> list:
    return data_from_file(filepath_data)


def get_example_data() -> list:
    return data_from_file(filepath_example)


def elapse_day(lanternfish: list) -> list:
    additional_fish = []

    for i, fish in enumerate(lanternfish):
        if fish == 0:
            lanternfish[i] = 6
            additional_fish.append(8)
        else:
            lanternfish[i] -= 1

    lanternfish.extend(additional_fish)
    return lanternfish


def init_efficiency_mode(lanternfish: list) -> list:
    fish_count_by_age = {n: 0 for n in range(0, 9)}

    for i, fish in enumerate(lanternfish):
        fish_count_by_age[fish] += 1

    return fish_count_by_age


def elapse_day_efficiently(fish_count_by_age: list) -> list:
    fish_count_by_age_next_day = {}

    for n in range(0, 9):
        fish_count_by_age_next_day[n] = fish_count_by_age[(n + 1) % 9]
    fish_count_by_age_next_day[6] += fish_count_by_age[0]

    return fish_count_by_age_next_day


def elapse_days(lanternfish: list, days: int, efficiently: bool = False) -> int:
    if not efficiently:
        for n in range(0, days):
            lanternfish = elapse_day(lanternfish)
        return len(lanternfish)
    else:
        lanternfish = init_efficiency_mode(lanternfish)
        for n in range(0, days):
            lanternfish = elapse_day_efficiently(lanternfish)
        return sum(x for x in lanternfish.values())


if __name__ == '__main__':
    print(day)
    part1 = elapse_days(get_input_data(), 80)
    print(f"Part 1: {part1}")
    part2 = elapse_days(get_input_data(), 256, efficiently=True)
    print(f"Part 2: {part2}")
    print()
