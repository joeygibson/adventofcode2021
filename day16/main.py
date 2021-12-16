#! /usr/bin/env python3
import sys
from typing import List

hex_map = {hex(i)[2:].upper(): bin(i)[2:].zfill(4) for i in range(0, 16)}


class Packet:
    def __init__(self, in_str="", as_bin=False) -> None:
        self.value = 0
        self.literal = 0
        self.version = 0
        self.type_id = None
        self.extra = ""
        self.children = []

        if not in_str or all(x == '0' for x in in_str):
            return
        if not as_bin:
            new = ""
            for i in range(len(in_str)):
                new += hex_map[in_str[i]]
            inp = new
        else:
            inp = in_str

        self.version = int(inp[:3], 2)
        self.type_id = int(inp[3:6], 2)
        self.inp = inp

        if self.type_id == 4:
            self.get_literal()
        else:
            self.get_ops()

    def __repr__(self) -> str:
        return f"{self.type_id=},{self.version=},{self.value=}"

    def get_literal(self):
        literal_val = self.inp[6:]
        literal_str = ''

        stop = False
        for i in range(0, len(literal_val), 5):
            if stop:
                break

            marker = literal_val[i]
            if marker == '0':
                stop = True

            substr = literal_val[i + 1: i + 5]
            literal_str += substr

        self.value = int(literal_str, 2)
        self.extra = self.inp[len(literal_str) + 6:]

    def get_ops(self):
        length_type = self.inp[6]

        if length_type == '0':
            data = self.inp[7:7+15]
            length_in_bits = int(data, 2)
            self.total_children_length = length_in_bits

            remaining = self.inp[22:22+length_in_bits]

            while remaining:
                temp = Packet(remaining, True)
                self.children.append(temp)
                remaining = temp.extra

            all_packets.extend(self.children)
            self.extra = self.inp[22 + length_in_bits:]
        elif length_type == '1':
            # next 11 bits
            data = self.inp[7:7 + 11]
            contains = int(data, 2)
            cur = self.inp[18:]
            self.num_children = contains
            used = 0
            for _ in range(contains):
                temp = Packet(cur, True)
                self.children.append(temp)
                cur = temp.extra
                used += len(cur)

            all_packets.extend(self.children)
            self.extra = cur
        else:
            assert False, length_type


all_packets = []


def get_data(path) -> str:
    with open(path) as f:
        return f.read().strip()


def get_version_and_type(binary: str) -> (int, int):
    p_version = int(binary[0:3], 2)
    p_type = int(binary[3:6], 2)

    return p_version, p_type


def process_literal(binary: str) -> (int, int, int):
    sv, _ = get_version_and_type(binary[0:5])
    literal_str = ''

    stop = False
    last_index = sys.maxsize
    for i in range(6, len(binary), 5):
        if stop:
            break

        marker = binary[i]
        if marker == '0':
            stop = True

        substr = binary[i + 1: i + 5]
        last_index = i + 5
        literal_str += substr

    literal = int(literal_str, 2)

    return sv, literal, last_index


def process_operator(binary: str) -> (List[int], int, List[int]):
    ov, _ = get_version_and_type(binary[0:5])
    versions = [ov]
    length_type = binary[6]
    sub_packets = []

    if length_type == '0':
        bits = binary[7:22]
        length = int(bits, 2)
        rest = binary[22:22 + length]

        while rest:
            sv, st = get_version_and_type(rest)
            if st == 4:
                version, literal, packet_length = process_literal(rest)
                versions.append(version)
                sub_packets.append(literal)
                if packet_length > 0:
                    rest = rest[packet_length:]
            else:
                pass
    else:
        bits = binary[7:18]
        subpackets = int(bits, 2)
        rest = binary[18:]

        for sub in range(subpackets):
            sv, st = get_version_and_type(rest)
            if st == 4:
                version, literal, packet_length = process_literal(rest)
                versions.append(version)

                sub_packets.append(literal)
                if packet_length > 0:
                    rest = rest[packet_length:]
            else:
                sub_versions, literal, packet_length = process_operator(rest)
                versions += sub_versions

                sub_packets.append(literal)
                # if packet_length > 0:
                #     rest = rest[packet_length:]

    return versions, -1, []


def part1(packets: str) -> int:
    binary = ''.join([hex_map[c] for c in packets])

    p = Packet(binary, True)
    print(p)
    #
    # p_version, p_type = get_version_and_type(binary[0:6])
    # print(f'p_version: {p_version}')
    # versions = []
    #
    # if p_type == 4:
    #     version, literal, packet_length = process_literal(binary)
    #     extra = binary[packet_length:]
    #     versions.append(version)
    #     print(f'{literal}, {packet_length}')
    # else:
    #     # operator
    #     sub_versions, op, vals = process_operator(binary)
    #     versions += sub_versions
    #
    # print(f'versions {versions}')
    # print(f'version count {len(versions)}')
    # return sum(versions)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print()
    # print(f'part2 {part2(*get_data(file_name))}')
