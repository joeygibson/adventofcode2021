#! /usr/bin/env python3
import sys
from functools import reduce


def get_data(path) -> list:
    with open(path) as f:
        return [int(x) for x in f.read().strip().split(',')]


def part1(lst: list[int]) -> int:
    least_fuel = sys.maxsize

    for pos in lst:
        fuel = reduce(lambda acc, x: acc + abs(x - pos), lst, 0)

        if fuel < least_fuel:
            least_fuel = fuel

    return least_fuel


def part2(lst: list[int]) -> int:
    least_fuel = sys.maxsize

    for pos in range(0, max(lst)):
        fuel = reduce(lambda acc, x: acc + step_mul(abs(x - pos)), lst, 0)
        if fuel < least_fuel:
            least_fuel = fuel

    return least_fuel


def step_mul(steps: int) -> int:
    return int((steps ** 2 + steps) / 2)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part 1: {part1(get_data(file_name))}')
    print(f'part 2: {part2(get_data(file_name))}')
