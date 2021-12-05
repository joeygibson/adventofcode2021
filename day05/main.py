#! /usr/bin/env python3
import itertools
import sys


def part1(lst: list) -> int:
    straight_lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lst))

    xs = [int(x[0][0]) for x in straight_lines] + [int(x[1][0]) for x in straight_lines]
    max_x = max(xs)
    ys = [int(x[0][1]) for x in straight_lines] + [int(x[1][1]) for x in straight_lines]
    max_y = max(ys)

    sea_map = {}
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            sea_map[(x, y)] = '.'

    for a, b in straight_lines:
        if a[0] == b[0]:
            step = 1 if a[1] < b[1] else -1
            line = [(a[0], y) for y in range(a[1], b[1] + step, step)]
        else:
            step = 1 if a[0] < b[0] else -1
            line = [(x, a[1]) for x in range(a[0], b[0] + step, step)]

        for pair in line:
            if sea_map[pair] == '.':
                sea_map[pair] = 1
            else:
                sea_map[pair] += 1

    return len(list(filter(lambda v: v != '.' and v > 1, sea_map.values())))


def part2(lst: list) -> int:
    xs = [int(x[0][0]) for x in lst] + [int(x[1][0]) for x in lst]
    max_x = max(xs)
    ys = [int(x[0][1]) for x in lst] + [int(x[1][1]) for x in lst]
    max_y = max(ys)

    sea_map = {}
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            sea_map[(x, y)] = '.'

    for a, b in lst:
        x_step = 1 if a[0] < b[0] else -1
        y_step = 1 if a[1] < b[1] else -1

        if a[0] == b[0]:
            fill_value = a[0]
        elif a[1] == b[1]:
            fill_value = a[1]
        else:
            fill_value = None

        co = list(itertools.zip_longest(range(a[0], b[0] + x_step, x_step), range(a[1], b[1] + y_step, y_step),
                                        fillvalue=fill_value))

        for pair in co:
            if sea_map[pair] == '.':
                sea_map[pair] = 1
            else:
                sea_map[pair] += 1

    return len(list(filter(lambda v: v != '.' and v > 1, sea_map.values())))


def get_data(path) -> list:
    with open(path) as f:
        raw = [x.strip().split(' -> ') for x in f.readlines() if x.strip()]
        return [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in raw]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])

    r1 = part1(lines)
    r2 = part2(lines)

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')
