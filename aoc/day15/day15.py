import operator

day = "day15"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Coords = tuple[int, int]
RiskMap = list[list[int]]


def data_from_file(filename: str) -> RiskMap:
    with open(filename) as f:
        return [[int(x) for x in list(line.strip())] for line in f]


def get_input_data() -> RiskMap:
    return data_from_file(filepath_data)


def get_example_data(n: int = 1) -> RiskMap:
    filename, suffix = filepath_example.split(".")
    return data_from_file(f"{filename}{n}.{suffix}")


def calc_lowest_route_risk(riskmap: RiskMap) -> int:
    x, y = (0, 0)

    predecessor_by_coords: dict[Coords, Coords] = {}
    risk_by_coords: dict[Coords, int] = {(0, 0): 0}
    priority_queue: dict[Coords, int] = {(0, 0): 0}

    max_x = len(riskmap) - 1
    max_y = len(riskmap[0]) - 1

    while (x, y) != (max_x, max_y):
        (x, y), risk_until_now = min(priority_queue.items(), key=operator.itemgetter(1))
        del priority_queue[(x, y)]

        neighbors_to_update: list[Coords] = []
        if x + 1 <= max_x:
            neighbors_to_update.append((x + 1, y))
        if y + 1 <= max_y:
            neighbors_to_update.append((x, y + 1))
        if x - 1 >= 0:
            neighbors_to_update.append((x - 1, y))
        if y - 1 >= 0:
            neighbors_to_update.append((x, y - 1))

        for n_x, n_y in neighbors_to_update:
            risk_new = risk_until_now + riskmap[n_x][n_y]
            if (n_x, n_y) not in risk_by_coords or risk_by_coords[(n_x, n_y)] > risk_new:
                priority_queue[(n_x, n_y)] = risk_new
                risk_by_coords[(n_x, n_y)] = risk_new
                predecessor_by_coords[(n_x, n_y)] = (x, y)

    return risk_by_coords[x, y]


def tile_riskmap(riskmap: RiskMap, times: int) -> RiskMap:
    len_x = len(riskmap)
    len_y = len(riskmap[0])
    riskmap_extended: RiskMap = []

    for x in range(0, times * len_x):
        riskmap_extended.append([])
        for y in range(0, times * len_y):
            if x >= len_x:
                val_new = (riskmap_extended[x - len_x][y] % 9) + 1
                riskmap_extended[x].append(val_new)
            elif y >= len_y:
                val_new = (riskmap_extended[x][y - len_y] % 9) + 1
                riskmap_extended[x].append(val_new)
            else:
                riskmap_extended[x].append(riskmap[x][y])

    return riskmap_extended


if __name__ == "__main__":
    print(day)
    part1 = calc_lowest_route_risk(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_lowest_route_risk(tile_riskmap(get_input_data(), 5))
    print(f"Part 2: {part2}")
    print()
