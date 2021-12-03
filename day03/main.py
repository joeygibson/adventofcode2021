#! /usr/bin/env python3
import sys
from functools import reduce
from typing import Callable


def partition(lst: list[str], pred: Callable[[str], bool]) -> (list[str], list[str]):
    return reduce(lambda x, y: x[pred(y)].append(y) or x, lst, ([], []))


def part1(lst: list) -> int:
    gamma = ''
    epsilon = ''

    for i in range(0, len(lst[0])):
        col = [x[i] for x in lines]
        ones, zeros = partition(col, lambda x: x == '0')

        if len(ones) > len(zeros):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def get_data(path):
    with open(path) as f:
        return [list(x.strip()) for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])

    r1 = part1(lines)
    # r2 = part2(lines)

    print(f'part 1: {r1}')
    # print(f'part 2: {r2}')
