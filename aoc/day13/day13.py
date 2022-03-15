from operator import itemgetter

day = "day13"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

Paper = list[list[str]]
Fold = tuple[str, int]

CHAR_DOT = "#"


def data_from_file(filename: str) -> tuple[Paper, list[Fold]]:
    with open(filename) as f:
        lines = [line.strip() for line in f]
        lines_dots = filter(lambda line: "," in line, lines)
        lines_folds = filter(lambda line: "fold" in line, lines)

        dot_coords: list[tuple[int, int]] = []
        for line in lines_dots:
            x, y = line.split(",")
            dot_coords.append((int(x), int(y)))

        max_x = max(dot_coords, key=itemgetter(0))[0]
        max_y = max(dot_coords, key=itemgetter(1))[1]

        paper: Paper = []
        for _ in range(0, max_y + 1):
            paper.append(["." for _ in range(0, max_x + 1)])

        for x, y in dot_coords:
            paper[y][x] = "#"

        folds: list[Fold] = []
        for line in lines_folds:
            axis, idx = line.split("fold along ")[1].split("=")
            folds.append((axis, int(idx)))

        return paper, folds


def get_input_data() -> tuple[Paper, list[Fold]]:
    return data_from_file(filepath_data)


def get_example_data() -> tuple[Paper, list[Fold]]:
    return data_from_file(filepath_example)


def print_paper(paper: Paper) -> None:
    for row in paper:
        print("".join(row))


def do_fold(paper: Paper, fold: Fold) -> Paper:
    fold_axis = fold[0]
    fold_idx = fold[1]
    paper_folded: Paper = []

    if fold_axis == "x":
        for y, _ in enumerate(paper):
            for x in range(0, fold_idx):
                left_side_is_dot = paper[y][x] == CHAR_DOT
                right_side_is_dot = paper[y][2 * fold_idx - x] == CHAR_DOT
                if not left_side_is_dot and right_side_is_dot:
                    paper[y][x] = CHAR_DOT
            paper_folded.append(paper[y][0:fold_idx])
    else:
        for y in range(0, fold_idx):
            for x, _ in enumerate(paper[y]):
                upper_side_is_dot = paper[y][x] == CHAR_DOT
                lower_side_is_dot = paper[2 * fold_idx - y][x] == CHAR_DOT
                if not upper_side_is_dot and lower_side_is_dot:
                    paper[y][x] = CHAR_DOT
            paper_folded.append(paper[y])

    return paper_folded


def do_folds(paper: Paper, folds: list[Fold], n_folds: int = -1) -> Paper:
    for fold_idx, fold in enumerate(folds):
        if n_folds != -1 and fold_idx >= n_folds:
            break
        paper = do_fold(paper, fold)

    return paper


def count_dots_after_folds(paper: Paper, folds: list[Fold], n_folds: int = -1) -> int:
    paper = do_folds(paper, folds, n_folds)

    dot_count = 0
    for row in paper:
        for cell in row:
            if cell == CHAR_DOT:
                dot_count += 1

    return dot_count


if __name__ == "__main__":
    print(day)
    paper, folds = get_input_data()
    part1 = count_dots_after_folds(paper, folds, 1)
    print(f"Part 1: {part1}")
    part2 = do_folds(paper, folds)
    print(f"Part 2")
    print_paper(part2)
    print()
