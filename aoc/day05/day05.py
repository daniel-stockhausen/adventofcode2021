import numpy as np
from scipy.sparse import dok_array

day = 'day05'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> dict:
    with open(filename) as f:
        lines = [line.strip() for line in f]
    return lines


def get_input_data() -> list:
    return data_from_file(filepath_data)


def get_example_data() -> list:
    return data_from_file(filepath_example)


def calc_diagram(vents: list, use_diagonals: bool = False) -> dict:
    matrix = dok_array((100, 100), dtype=np.int8)

    for vent in vents:
        coords_start, coords_end = vent.split(' -> ')
        x1, y1 = [int(n) for n in coords_start.split(',')]
        x2, y2 = [int(n) for n in coords_end.split(',')]

        if max(x1, x2) >= matrix.shape[0]:
            matrix.resize(round(max(x1, x2) + 50, -2), matrix.shape[1])
        if max(y1, y2) >= matrix.shape[1]:
            matrix.resize(matrix.shape[0], round(max(y1, y2) + 50, -2))

        is_diagonal = max(x1, x2) - min(x1, x2) == max(y1, y2) - min(y1, y2)

        if use_diagonals and is_diagonal:
            for x in range(0, max(x1, x2) - min(x1, x2) + 1):
                sign_x = 1 if x1 <= x2 else -1
                sign_y = 1 if y1 <= y2 else -1
                matrix[x1 + sign_x * x, y1 + sign_y * x] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix[x, y1] += 1

    return dict(matrix)


def count_overlapping_coords(vents: list, use_diagonals: bool = False) -> int:
    matrix_dict = calc_diagram(vents, use_diagonals)
    return sum(1 for n in matrix_dict.values() if n >= 2)


if __name__ == '__main__':
    print(day)
    part1 = count_overlapping_coords(get_input_data())
    print(f"Part 1: {part1}")
    part2 = count_overlapping_coords(get_input_data(), use_diagonals=True)
    print(f"Part 2: {part2}")
    print()
