#! /usr/bin/env python3
import sys


def part1(lst: list) -> int:
    horiz_ops = filter(lambda x: x[0] == 'forward', lst)
    vert_ops = filter(lambda x: x[0] != 'forward', lst)

    horizontal = sum([int(x[1]) for x in horiz_ops])
    vertical = sum([int(x[1]) if x[0] == 'down' else -int(x[1]) for x in vert_ops])

    return horizontal * vertical


def part2(lst: list) -> int:
    pos = 0
    depth = 0
    aim = 0

    for op, val in lst:
        val = int(val)

        if op == 'forward':
            pos += val
            depth += aim * val
        elif op == 'up':
            aim -= val
        else:
            aim += val

    return depth * pos


def get_data(path):
    with open(path) as f:
        return [x.strip().split() for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])

    r1 = part1(lines)
    r2 = part2(lines)

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')
