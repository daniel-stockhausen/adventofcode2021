day = "day11"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Coordinate = tuple[int, int]
CoordList = list[Coordinate]
OctopusMap = list[list[int]]


class OctopusLevels:
    def __init__(self, map_str: str) -> None:
        self.map = map_str

    @property
    def map(self) -> OctopusMap:
        return self._map

    @map.setter
    def map(self, value: str) -> None:
        self._map = [[int(x) for x in list(line)] for line in value.split()]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, OctopusLevels):
            return self.map == other.map
        else:
            return False

    def __repr__(self) -> str:
        output = ""
        for line_lst in self._map:
            output += "".join([str(n) for n in line_lst]) + "\n"
        output = output[:-1]
        return output


def data_from_file(filename: str) -> OctopusLevels:
    with open(filename) as f:
        return OctopusLevels("".join(f.readlines()))


def get_input_data() -> OctopusLevels:
    return data_from_file(filepath_data)


def get_example_data() -> OctopusLevels:
    return data_from_file(filepath_example)


def increase_level(x: int, y: int, lvls: OctopusLevels, flash_done: CoordList, flash_next: CoordList) -> OctopusLevels:
    map = lvls.map
    coord = (x, y)
    if coord not in flash_done:
        level_new = map[x][y] + 1
        if level_new > 9:
            flash_next.append(coord)
        map[x][y] = level_new

    return lvls


def process_step_count_flashes(lvls: OctopusLevels) -> int:
    map = lvls.map
    flash_done: list[Coordinate] = []
    flash_next: list[Coordinate] = []

    for x, line in enumerate(map):
        for y, _ in enumerate(line):
            increase_level(x, y, lvls, flash_done, flash_next)

    max_x = len(map) - 1
    max_y = len(map[0]) - 1

    while len(flash_next) > 0:
        coords_flash = flash_next
        flash_next = []
        for x, y in coords_flash:
            flash_done.append((x, y))
            map[x][y] = 0

            if x + 1 <= max_x:
                increase_level(x + 1, y, lvls, flash_done, flash_next)
            if y + 1 <= max_y:
                increase_level(x, y + 1, lvls, flash_done, flash_next)
            if x - 1 >= 0:
                increase_level(x - 1, y, lvls, flash_done, flash_next)
            if y - 1 >= 0:
                increase_level(x, y - 1, lvls, flash_done, flash_next)
            if x + 1 <= max_x and y + 1 <= max_y:
                increase_level(x + 1, y + 1, lvls, flash_done, flash_next)
            if x + 1 <= max_x and y - 1 >= 0:
                increase_level(x + 1, y - 1, lvls, flash_done, flash_next)
            if x - 1 >= 0 and y + 1 <= max_y:
                increase_level(x - 1, y + 1, lvls, flash_done, flash_next)
            if x - 1 >= 0 and y - 1 >= 0:
                increase_level(x - 1, y - 1, lvls, flash_done, flash_next)

        flash_next = list(set(flash_next) - set(flash_done))

    return len(flash_done)


def count_flashes_for_steps(steps: int, lvls: OctopusLevels) -> int:
    flash_count = 0
    for _ in range(0, steps):
        flash_count += process_step_count_flashes(lvls)

    return flash_count


def calc_synchronized_step(lvls: OctopusLevels) -> int:
    step = 1
    octopus_count = len(lvls.map) * len(lvls.map[0])
    while process_step_count_flashes(lvls) != octopus_count:
        step += 1

    return step


if __name__ == "__main__":
    print(day)
    part1 = count_flashes_for_steps(100, get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_synchronized_step(get_input_data())
    print(f"Part 2: {part2}")
    print()
