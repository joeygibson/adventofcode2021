#! /usr/bin/env python3
import sys

from collections import deque


def get_data(path) -> (list[list[int]]):
    with open(path) as f:
        lines = f.readlines()

    return [[int(i) for i in r.strip()] for r in lines]


def part1(x: list[list[int]]) -> int:
    t = 1e99

    q = deque([(0, 0, 0)])
    v = set()

    while q:
        a, b, c = q.popleft()

        if (a, b, c) in v:
            continue

        v.add((a, b, c))

        if (a, b) == (len(x) - 1, len(x[0]) - 1):
            t = min(t, c)
            continue

        try:
            q.append((a + 1, b, c + x[a + 1][b]))
        except:
            pass

        try:
            q.append((a, b + 1, c + x[a][b + 1]))
        except:
            pass

    return t


# def part1(the_map: dict[Tuple[int, int], int]) -> int:
# start = min(the_map.keys())
# goal = max(the_map.keys())
#
# current = start
# path = []
#
# while current != goal:
#     x, y = current
#
#     neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
#     neighbors_and_vals = {n: the_map.get(n) for n in neighbors if the_map.get(n) is not None}
#
#     low_risk_neighbors = []
#
#     for n, val in neighbors_and_vals.items():
#         if val < low_val:
#             low_val = val
#             low_key = n
#
#     path.append(low_key)
#     current = low_key


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print()
    # print(f'part2 {part2(*get_data(file_name))}')
