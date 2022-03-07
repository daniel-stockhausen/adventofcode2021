day = 'day02'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> list[tuple[str, int]]:
    cmds: list[tuple[str, int]] = []
    with open(filename) as f:
        for line in f:
            cmd_pair = line.split()
            cmds.append((cmd_pair[0], int(cmd_pair[1])))
    return cmds


def get_input_data() -> list[tuple[str, int]]:
    return data_from_file(filepath_data)


def get_example_data() -> list[tuple[str, int]]:
    return data_from_file(filepath_example)


def calculate_destination(cmds: list[tuple[str, int]]) -> int:
    pos = 0
    depth = 0

    for operation, operand in cmds:
        match operation:
            case 'forward':
                pos += operand
            case 'up':
                depth -= operand
            case 'down':
                depth += operand
            case _:
                pass

    return pos * depth


def calculate_destination_part2(cmds: list[tuple[str, int]]) -> int:
    pos = 0
    depth = 0
    aim = 0

    for operation, operand in cmds:
        match operation:
            case 'forward':
                pos += operand
                depth += aim * operand
            case 'up':
                aim -= operand
            case 'down':
                aim += operand
            case _:
                pass

    return pos * depth


if __name__ == '__main__':
    print(day)
    part1 = calculate_destination(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calculate_destination_part2(get_input_data())
    print(f"Part 2: {part2}")
    print()
