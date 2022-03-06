import numpy as np

day = 'day03'
filepath_data = f'input/{day}.txt'
filepath_example = f'input/{day}-example.txt'


def data_from_file(filename: str) -> list:
    bits_matrix = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            list_of_bits = list(line)
            bits_matrix.append(list_of_bits)

    return bits_matrix


def get_input_data() -> list:
    return data_from_file(filepath_data)


def get_example_data() -> list:
    return data_from_file(filepath_example)


def calc_power_consumption(bits_matrix: list) -> int:
    gamma_rate = ''
    epsilon_rate = ''

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


def extract_most_common_bits(bits_matrix: list, least_common_bits_mode: bool = False) -> int:
    bits_matrix = np.array(bits_matrix)
    column_count = bits_matrix.shape[1]
    for n1 in range(0, column_count):
        indices_zero = []
        indices_one = []

        row_count = bits_matrix.shape[0]
        if row_count == 1:
            break
        for n2 in range(0, row_count):
            if bits_matrix[n2, n1] == '0':
                indices_zero.append(n2)
            elif bits_matrix[n2, n1] == '1':
                indices_one.append(n2)

        if not least_common_bits_mode:
            if len(indices_zero) > len(indices_one):
                bits_matrix = np.delete(bits_matrix, indices_one, axis=0)
            elif len(indices_zero) <= len(indices_one):
                bits_matrix = np.delete(bits_matrix, indices_zero, axis=0)
        else:
            if len(indices_zero) <= len(indices_one):
                bits_matrix = np.delete(bits_matrix, indices_one, axis=0)
            elif len(indices_zero) > len(indices_one):
                bits_matrix = np.delete(bits_matrix, indices_zero, axis=0)

    bit_string = ''.join(bits_matrix.tolist()[0])
    return int(bit_string, 2)


def calc_oxygen_generator_rating(bits_matrix: list) -> int:
    return extract_most_common_bits(bits_matrix, least_common_bits_mode=False)


def calc_co2_scrubber_rating(bits_matrix: list) -> int:
    return extract_most_common_bits(bits_matrix, least_common_bits_mode=True)


def calc_life_support_rating(bits_matrix: list) -> int:
    return calc_oxygen_generator_rating(bits_matrix) * calc_co2_scrubber_rating(bits_matrix)


if __name__ == '__main__':
    print(day)
    part1 = calc_power_consumption(get_input_data())
    print(f"Part 1: {part1}")
    part2 = calc_life_support_rating(get_input_data())
    print(f"Part 2: {part2}")
    print()
