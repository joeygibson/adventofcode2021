#! /usr/bin/env python3
import sys
from typing import List

hex_map = {hex(i)[2:].upper(): bin(i)[2:].zfill(4) for i in range(0, 16)}


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

    p_version, p_type = get_version_and_type(binary[0:6])
    print(f'p_version: {p_version}')
    versions = []

    if p_type == 4:
        version, literal, packet_length = process_literal(binary)
        extra = binary[packet_length:]
        versions.append(version)
        print(f'{literal}, {packet_length}')
    else:
        # operator
        sub_versions, op, vals = process_operator(binary)
        versions += sub_versions

    print(f'versions {versions}')
    print(f'version count {len(versions)}')
    return sum(versions)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print()
    # print(f'part2 {part2(*get_data(file_name))}')
