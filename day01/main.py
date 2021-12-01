#! /usr/bin/env python3
import sys


def part1(path: str) -> int:
    with open(path) as f:
        lines = [int(x) for x in f.readlines()]

    res = [ind + 1 for ind, x in enumerate(lines) if ind + 1 < len(lines) and lines[ind + 1] > x]
    return len(res)


def part2(path: str) -> int:
    with open(path) as f:
        lines = [int(x) for x in f.readlines()]

    groups = [x + lines[ind + 1] + lines[ind + 2] for ind, x in enumerate(lines) if ind + 2 < len(lines)]
    res = [ind + 1 for ind, x in enumerate(groups) if ind + 1 < len(groups) and groups[ind + 1] > x]
    return len(res)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    r1 = part1(sys.argv[1])
    r2 = part2(sys.argv[1])

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')
