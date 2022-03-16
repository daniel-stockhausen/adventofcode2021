import os
import unittest

from aoc.day16.day16 import Packet, get_example_data, get_input_data, hex_to_bin, parse_hex, \
    sum_version_numbers


class TestDay16(unittest.TestCase):
    def test_packet_eq(self):
        packet1 = Packet(1, 2, 42)
        packet2 = Packet(9, 10, 99)
        self.assertEqual(packet1, Packet(1, 2, 42))
        self.assertEqual(Packet(3, 4, [packet1, packet2]), Packet(3, 4, [packet1, packet2]))
        self.assertNotEqual(packet1, Packet(3, 2, 42))
        self.assertNotEqual(packet1, Packet(1, 4, 42))
        self.assertNotEqual(packet1, Packet(1, 2, 43))
        self.assertNotEqual(packet1, 7)

    def test_hex_to_bin(self):
        self.assertEqual("110100101111111000101000", hex_to_bin("D2FE28"))
        self.assertEqual("00111000000000000110111101000101001010010001001000000000", hex_to_bin("38006F45291200"))
        self.assertEqual("11101110000000001101010000001100100000100011000001100000", hex_to_bin("EE00D40C823060"))

    def test_parse_packet(self):
        self.assertEqual(Packet(6, 4, 2021), parse_hex("D2FE28"))
        self.assertEqual(Packet(1, 6, [Packet(6, 4, 10), Packet(2, 4, 20)]),
                         parse_hex("38006F45291200"))
        self.assertEqual(Packet(7, 3, [Packet(2, 4, 1), Packet(4, 4, 2), Packet(1, 4, 3)]),
                         parse_hex("EE00D40C823060"))

    def test_16a_example(self):
        self.assertEqual(16, sum_version_numbers(get_example_data(1)))
        self.assertEqual(12, sum_version_numbers(get_example_data(2)))
        self.assertEqual(23, sum_version_numbers(get_example_data(3)))
        self.assertEqual(31, sum_version_numbers(get_example_data(4)))

    def test_16a(self):
        self.assertEqual(993, sum_version_numbers(get_input_data()))

    def test_16b_example(self):
        self.assertEqual(4, parse_hex("4200940C83").eval())
        self.assertEqual(3, parse_hex("C200B40A82").eval())
        self.assertEqual(54, parse_hex("04005AC33890").eval())
        self.assertEqual(7, parse_hex("880086C3E88112").eval())
        self.assertEqual(9, parse_hex("CE00C43D881120").eval())
        self.assertEqual(1, parse_hex("D8005AC2A8F0").eval())
        self.assertEqual(0, parse_hex("F600BC2D8F").eval())
        self.assertEqual(0, parse_hex("9C005AC2F8F0").eval())
        self.assertEqual(1, parse_hex("9C0141080250320F1802104A08").eval())

    def test_16b(self):
        self.assertEqual(144595909277, get_input_data().eval())

    def test_16_main(self):
        self.assertEqual(0, os.system("python -m aoc.day16.day16"))
