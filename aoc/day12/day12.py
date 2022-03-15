day = "day12"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Connections = dict[str, set[str]]

NODE_START = "start"
NODE_END = "end"


def data_from_file(filename: str) -> Connections:
    with open(filename) as f:
        conns: Connections = dict()
        for line in f:
            a, b = line.strip().split("-")
            for x in (a, b):
                if x not in conns:
                    conns[x] = set()

            if a != NODE_END and b != NODE_START:
                conns[a].add(b)
            if b != NODE_END and a != NODE_START:
                conns[b].add(a)

        for key, val in conns.items():
            conns[key] = set(val)

        return conns


def get_input_data() -> Connections:
    return data_from_file(filepath_data)


def get_example_data(n: int = 3) -> Connections:
    filename, suffix = filepath_example.split(".")
    return data_from_file(f"{filename}{n}.{suffix}")


def build_paths_from(start: str, conns: Connections, exclusions: set[str], dupe: str | None = None) -> list[str]:
    paths: list[str] = []
    options = conns[start].copy()
    options -= exclusions

    for option in options:
        exclusions_new = exclusions.copy()
        if option.islower() and not option == "end":
            exclusions_new.add(option)
        for suffix in build_paths_from(option, conns, exclusions_new, dupe):
            paths.append(f"{start},{suffix}")

    if dupe == "":
        dupe_options = conns[start].copy() - options
        for option in dupe_options:
            for suffix in build_paths_from(option, conns, exclusions.copy(), option):
                paths.append(f"{start},{suffix}")

    if start == NODE_END:
        return ["end"]
    else:
        return paths


def count_valid_paths(conns: Connections, allow_single_dupe: bool = False) -> int:
    paths = build_paths_from(NODE_START, conns, set(), "" if allow_single_dupe else None)
    return len(paths)


if __name__ == "__main__":
    print(day)
    part1 = count_valid_paths(get_input_data())
    print(f"Part 1: {part1}")
    part2 = count_valid_paths(get_input_data(), allow_single_dupe=True)
    print(f"Part 2: {part2}")
    print()
