#! /usr/bin/env python3
import sys
from functools import reduce


def get_data(path) -> list:
    data = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            data.append([x.split() for x in line.split('|')])

    return data


def part1(lst: list[list[str]]) -> int:
    res = 0
    for row in lst:
        for display in row[1]:
            segments = len(display)
            print(f'{display} {segments}')
            if segments == 2 or segments == 3 or segments == 4 or segments == 7:
                res += 1

    return res



def part2(lst: list[int]) -> int:
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)
    print(f'data: {data}')
    print(f'part 1: {part1(get_data(file_name))}')
    # print(f'part 2: {part2(get_data(file_name))}')
