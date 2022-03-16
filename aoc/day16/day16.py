from __future__ import annotations

import math
from typing import Any

day = "day16"
filepath_data = f"input/{day}.txt"
filepath_example = f"input/{day}-example.txt"

bin_by_hex_str: dict[str, str] = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


class Packet:
    version: int = -1
    type: int = -1
    value: int | list[Packet] = -1

    def __init__(self, version: int, type: int, value: int | list[Packet]) -> None:
        self.version = version
        self.type = type
        self.value = value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Packet):
            return ((self.version, self.type, self.value)
                    == (other.version, other.type, other.value))
        else:
            return False

    def __int__(self) -> int:
        return self.eval()

    def __lt__(self, other: Any) -> bool:
        return self.value < other

    def __gt__(self, other: Any) -> bool:
        return self.value > other

    def eval(self) -> int:
        match self.type:
            case 0:
                return sum([int(sub_packet) for sub_packet in self.value])
            case 1:
                return math.prod([int(sub_packet) for sub_packet in self.value])
            case 2:
                return int(min(self.value))
            case 3:
                return int(max(self.value))
            case 4:
                return self.value
            case 5:
                return int(self.value[0]) > int(self.value[1])
            case 6:
                return int(self.value[0]) < int(self.value[1])
            case 7:
                return int(self.value[0]) == int(self.value[1])
            case _:
                raise ValueError("Invalid type id!")


def hex_to_bin(hex: str) -> str:
    return "".join([bin_by_hex_str[x] for x in hex])


def bin_to_dec(bin: str) -> int:
    return int(bin, 2)


def parse_hex(hex: str) -> Packet:
    packet_lst, _ = parse_bin(hex_to_bin(hex))
    return packet_lst[0]


def parse_bin(input_bin: str, max_packet: int = -1) -> tuple[list[Packet], str]:
    if max_packet == 0:
        return [], input_bin

    input_is_all_zeros_or_empty = input_bin == len(input_bin) * "0"
    if input_is_all_zeros_or_empty:
        return [], ""

    version = bin_to_dec(input_bin[:3])
    type = bin_to_dec(input_bin[3:6])

    payload = input_bin[6:]

    if type == 4:
        len_group = 5
        number_bit_str = ""
        groups = [payload[n:n + len_group] for n in range(0, len(payload), len_group)]
        for idx, group in enumerate(groups):
            if group[0] == "1" or group[0] == "0":
                number_bit_str += group[1:]
            else:
                raise ValueError("Invalid group type!")
            if group[0] == "0":
                payload = payload[(idx + 1) * len_group:]
                break
        value = bin_to_dec(number_bit_str)
    else:
        length_type = payload[:1]
        payload = payload[1:]
        if length_type == "0":
            sub_packets_length = bin_to_dec(payload[:15])
            payload = payload[15:]
            sub_packets_bit_str = payload[:sub_packets_length]
            payload = payload[sub_packets_length:]
            value, _ = parse_bin(sub_packets_bit_str)
        elif length_type == "1":
            sub_packet_count = bin_to_dec(payload[:11])
            payload = payload[11:]
            value, payload = parse_bin(payload, max_packet=sub_packet_count)
        else:
            raise ValueError("Invalid length type!")

    packets = [Packet(version, type, value)]
    if max_packet > -1:
        max_packet -= 1
    packet_lst, payload = parse_bin(payload, max_packet=max_packet)
    packets.extend(packet_lst)

    return packets, payload


def data_from_file(filename: str) -> Packet:
    with open(filename) as f:
        line = f.readline().strip()
        return parse_hex(line)


def get_input_data() -> Packet:
    return data_from_file(filepath_data)


def get_example_data(n: int) -> Packet:
    filename, suffix = filepath_example.split(".")
    return data_from_file(f"{filename}{n}.{suffix}")


def sum_version_numbers(packet: Packet) -> int:
    sum_versions = packet.version
    if isinstance(packet.value, list):
        for packet in packet.value:
            sum_versions += sum_version_numbers(packet)

    return sum_versions


if __name__ == "__main__":
    print(day)
    part1 = sum_version_numbers(get_input_data())
    print(f"Part 1: {part1}")
    part2 = get_input_data().eval()
    print(f"Part 2: {part2}")
    print()
