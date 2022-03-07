import numpy as np
import numpy.typing as npt

day = 'day03'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> list[list[str]]:
    bits_matrix: list[list[str]] = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            list_of_bits = list(line)
            bits_matrix.append(list_of_bits)

    return bits_matrix


def get_input_data() -> list[list[str]]:
    return data_from_file(filepath_data)


def get_example_data() -> list[list[str]]:
    return data_from_file(filepath_example)


def calc_power_consumption(bits_matrix: list[list[str]]) -> int:
    gamma_rate, gamma_rate_int = '', 0
    epsilon_rate, epsilon_rate_int = '', 0

    bits_matrix_transposed = np.array(bits_matrix).T.tolist()

    for column in bits_matrix_transposed:
        count_zero = column.count('0')
        count_one = column.count('1')

        if count_zero > count_one:
            gamma_rate += str('0')
            epsilon_rate += str('1')
        else:
            gamma_rate += str('1')
            epsilon_rate += str('0')

        gamma_rate_int = int(gamma_rate, 2)
        epsilon_rate_int = int(epsilon_rate, 2)

    return gamma_rate_int * epsilon_rate_int


def extract_most_common_bits(bits_matrix: list[list[str]], least_common_bits_mode: bool = False) -> int:
    bits_matrix_nd: npt.NDArray[np.int_] = np.array(bits_matrix)
    column_count = bits_matrix_nd.shape[1]
    for n1 in range(0, column_count):
        indices_zero: list[int] = []
        indices_one: list[int] = []

        row_count = bits_matrix_nd.shape[0]
        if row_count == 1:
            break
        for n2 in range(0, row_count):
            if bits_matrix_nd[n2, n1] == '0':
                indices_zero.append(n2)
            elif bits_matrix_nd[n2, n1] == '1':
                indices_one.append(n2)

        if not least_common_bits_mode:
            if len(indices_zero) > len(indices_one):
                bits_matrix_nd = np.delete(bits_matrix_nd, indices_one, axis=0)
            elif len(indices_zero) <= len(indices_one):
                bits_matrix_nd = np.delete(bits_matrix_nd, indices_zero, axis=0)
        else:
            if len(indices_zero) <= len(indices_one):
                bits_matrix_nd = np.delete(bits_matrix_nd, indices_one, axis=0)
            elif len(indices_zero) > len(indices_one):
                bits_matrix_nd = np.delete(bits_matrix_nd, indices_zero, axis=0)

    bit_string = ''.join(bits_matrix_nd.tolist()[0])
    return int(bit_string, 2)


def calc_oxygen_generator_rating(bits_matrix: list[list[str]]) -> int:
    return extract_most_common_bits(bits_matrix, least_common_bits_mode=False)


def calc_co2_scrubber_rating(bits_matrix: list[list[str]]) -> int:
    return extract_most_common_bits(bits_matrix, least_common_bits_mode=True)


def calc_life_support_rating(bits_matrix: list[list[str]]) -> int:
    return calc_oxygen_generator_rating(bits_matrix) * calc_co2_scrubber_rating(bits_matrix)


if __name__ == '__main__':
    print(day)
    part1 = calc_power_consumption(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_life_support_rating(get_input_data())
    print(f"Part 2: {part2}")
    print()
