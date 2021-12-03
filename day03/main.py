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
        col = [x[i] for x in lst]
        ones, zeros = partition(col, lambda x: x == '0')

        if len(ones) > len(zeros):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(lst: list) -> int:
    def part2_work(lst: list, index: int, ox: bool) -> int:
        for i in range(0, len(lst[0])):
            col = [x[index] for x in lst]
            ones, zeros = partition(col, lambda x: x == '0')

            if ox:
                val_to_keep = '1' if len(ones) > len(zeros) or len(ones) == len(zeros) else '0'
            else:
                val_to_keep = '0' if len(ones) > len(zeros) or len(ones) == len(zeros) else '1'

            filtered_list = list(filter(lambda x: x[index] == val_to_keep, lst))

            if len(filtered_list) == 1:
                return int(''.join(filtered_list[0]), 2)
            else:
                return part2_work(filtered_list, index + 1, ox)

    ox_rating = part2_work(lst, 0, True)
    co2_rating = part2_work(lst, 0, False)

    return ox_rating * co2_rating


def get_data(path):
    with open(path) as f:
        return [list(x.strip()) for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])

    r1 = part1(lines)
    r2 = part2(lines)

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')

# if len(ones) > len(zeros):
#     val_to_keep = '1'
# elif len(ones) < len(zeros):
#     val_to_keep = '0'
# else:
#     if ox:
#         val_to_keep = '1'
#     else:
#         val_to_keep = '0'
