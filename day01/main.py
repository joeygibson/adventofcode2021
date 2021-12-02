#! /usr/bin/env python3
import sys


def partition(lst: list, n: int) -> list:
    for i in range(0, len(lst)):
        yield lst[i:i + n]


def part1(lst: list) -> int:
    filtered_list = filter(lambda x: len(x) == 2, partition(lst, 2))
    res = [x for x, y in filtered_list if y > x]
    return len(res)


def part2(lst: list) -> int:
    groups = list(map(lambda x: sum(x), partition(lst, 3)))
    return part1(groups)


def get_data(path):
    with open(path) as f:
        return [int(x.strip()) for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])

    r1 = part1(lines)
    r2 = part2(lines)

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')
