from functools import reduce

day = "day09"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Heightmap = list[list[int]]
Coordinate = tuple[int, int]

_checked_coordinates: list[Coordinate] = []


def data_from_file(filename: str) -> Heightmap:
    with open(filename) as f:
        return [[int(x) for x in list(line.strip())] for line in f]


def get_input_data() -> Heightmap:
    return data_from_file(filepath_data)


def get_example_data() -> Heightmap:
    return data_from_file(filepath_example)


def is_low_point(x: int, y: int, heightmap: Heightmap) -> bool:
    max_x = len(heightmap) - 1
    max_y = len(heightmap[0]) - 1

    is_low_point = True
    if x + 1 <= max_x and not heightmap[x][y] < heightmap[x + 1][y]:
        is_low_point = False
    if x - 1 >= 0 and not heightmap[x][y] < heightmap[x - 1][y]:
        is_low_point = False
    if y + 1 <= max_y and not heightmap[x][y] < heightmap[x][y + 1]:
        is_low_point = False
    if y - 1 >= 0 and not heightmap[x][y] < heightmap[x][y - 1]:
        is_low_point = False

    return is_low_point


def sum_risk_levels_of_low_points(heightmap: Heightmap) -> int:
    risk_level_sum = 0
    for pos_x, line in enumerate(heightmap):
        for pos_y, height in enumerate(line):
            if is_low_point(pos_x, pos_y, heightmap):
                risk_level_sum += height + 1

    return risk_level_sum


def aggregate_basin_coords(x: int, y: int, heightmap: Heightmap, init: bool = True) -> list[Coordinate]:
    """Should be called with coordinates of low point of basin"""
    global _checked_coordinates
    if init is True:
        _checked_coordinates = []

    if (x, y) in _checked_coordinates or heightmap[x][y] == 9:
        return []
    else:
        _checked_coordinates.append((x, y))

    max_x = len(heightmap) - 1
    max_y = len(heightmap[0]) - 1

    if x + 1 <= max_x:
        aggregate_basin_coords(x + 1, y, heightmap, init=False)
    if y + 1 <= max_y:
        aggregate_basin_coords(x, y + 1, heightmap, init=False)
    if x - 1 >= 0:
        aggregate_basin_coords(x - 1, y, heightmap, init=False)
    if y - 1 >= 0:
        aggregate_basin_coords(x, y - 1, heightmap, init=False)

    if init is True:
        return sorted(_checked_coordinates)
    else:
        return []


def calc_basin_size(x: int, y: int, heightmap: Heightmap) -> int:
    return len(aggregate_basin_coords(x, y, heightmap))


def calc_basin_sizes(heightmap: Heightmap) -> list[int]:
    basin_sizes: list[int] = []
    for pos_x, line in enumerate(heightmap):
        for pos_y, _ in enumerate(line):
            if is_low_point(pos_x, pos_y, heightmap):
                basin_sizes.append((calc_basin_size(pos_x, pos_y, heightmap)))

    return basin_sizes


def multiply_three_largest_basins_size(heightmap: Heightmap) -> int:
    basin_sizes = calc_basin_sizes(heightmap)
    three_largest_sizes = sorted(basin_sizes)[-3:]

    return reduce(lambda a, b: a * b, three_largest_sizes)


if __name__ == "__main__":
    print(day)
    part1 = sum_risk_levels_of_low_points(get_input_data())
    print(f"Part 1: {part1}")
    part2 = multiply_three_largest_basins_size(get_input_data())
    print(f"Part 2: {part2}")
    print()
