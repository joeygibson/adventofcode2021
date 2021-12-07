#! /usr/bin/env python3
import statistics
import sys
from functools import reduce


def get_data(path) -> list:
    with open(path) as f:
        return [int(x) for x in f.read().strip().split(',')]


def part1(lst: list[int]) -> int:
    print(f'stddev {statistics.stdev(lst)}')
    print(f'mean {statistics.mean(lst)}')
    print(f'mode {statistics.mode(lst)}')
    print(f'variance {statistics.variance(lst)}')
    print(f'len {len(lst)}')

    mode = statistics.mode(lst)

    # fuel = reduce(lambda acc, x: acc + abs(x - mode), lst, 0)

    least_fuel = sys.maxsize
    best_pos = sys.maxsize

    for pos in lst:
        fuel = reduce(lambda acc, x: acc + abs(x - pos), lst, 0)

        if fuel < least_fuel:
            least_fuel = fuel
            best_pos = pos

    print(f'least_fuel {least_fuel}')
    print(f'best_pos {best_pos}')

    return least_fuel


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    r1 = part1(get_data(file_name))

    print(f'part 1: {r1}')
    # print(f'part 2: {r2}')
