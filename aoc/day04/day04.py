day = 'day04'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> tuple[list, list]:
    boards = []

    with open(filename) as f:
        drawn_numbers_line = f.readline().strip()
        drawn_numbers = drawn_numbers_line.split(',')

        board = []
        board_row_index = 0
        for line in f:
            board_row_index += 1
            if board_row_index == 1:
                continue

            board.append(line.split())

            if board_row_index == 6:
                boards.append(board)
                board = []
                board_row_index = 0
                continue

    return drawn_numbers, boards


def get_input_data() -> tuple[list, list]:
    return data_from_file(filepath_data)


def get_example_data() -> tuple[list, list]:
    return data_from_file(filepath_example)


def draw_number(drawn_number: str, boards: list, last_winning_board_mode: bool = False) -> tuple[int, list]:
    board_idxs_to_ignore = []

    for board_idx, board in enumerate(boards):
        if board_idx in board_idxs_to_ignore:
            continue

        for row_idx, row in enumerate(board):
            if board_idx in board_idxs_to_ignore:
                continue

            for column_idx, number in enumerate(row):
                if board_idx in board_idxs_to_ignore:
                    continue

                if number == drawn_number:
                    boards[board_idx][row_idx][column_idx] = 'x'
                    if has_board_won(board, column_idx, row_idx):
                        is_last_winning_board_mode_and_last_board = last_winning_board_mode and len(boards) == 1
                        if not last_winning_board_mode or is_last_winning_board_mode_and_last_board:
                            return calc_score_of_board(board, int(drawn_number)), boards
                        else:  # last_winning_board_mode but there is more than one board left
                            board_idxs_to_ignore.append(board_idx)

    board_idxs_to_ignore = list(set(board_idxs_to_ignore))
    board_idxs_to_ignore.sort(reverse=True)
    for board_idx in board_idxs_to_ignore:
        del boards[board_idx]

    return 0, boards


def has_board_won(board: list, column_idx: int, row_idx: int) -> bool:
    won_horizontal = True
    for n in range(0, 5):
        if board[row_idx][n] != 'x':
            won_horizontal = False
            break

    won_vertical = True
    for n in range(0, 5):
        if board[n][column_idx] != 'x':
            won_vertical = False
            break

    return won_horizontal or won_vertical


def calc_score_of_board(board: list, last_drawn: int) -> int:
    sum = 0
    for row in board:
        for n in row:
            if n != 'x':
                sum += int(n)

    return sum * last_drawn


def calc_score_of_winning_board(draw_numbers: list, boards: list, last_winning_board_mode: bool = False) -> int:
    boards_left = boards
    for n in draw_numbers:
        score, boards_left = draw_number(n, boards_left, last_winning_board_mode)
        if score > 0:
            return score

    return 0


if __name__ == '__main__':
    print(day)
    draw_numbers, boards = get_input_data()
    part1 = calc_score_of_winning_board(draw_numbers, boards)
    print(f"Part 1: {part1}")
    draw_numbers, boards = get_input_data()
    part2 = calc_score_of_winning_board(draw_numbers, boards, last_winning_board_mode=True)
    print(f"Part 2: {part2}")
    print()
