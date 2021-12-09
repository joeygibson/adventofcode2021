#! /usr/bin/env python3
import sys
from typing import Tuple


def is_low_point(sea_floor_map: dict, point: Tuple[int, int]) -> bool:
    point_depth = sea_floor_map[point]
    x, y = point

    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    depths = [sea_floor_map.get(n) for n in neighbors]
    valid_depths = list(filter(lambda d: d is not None, depths))
    low_points = list(filter(lambda d: d <= point_depth, valid_depths))

    print(f'point {point}, point_depth {point_depth}, low_points {low_points}')

    return len(low_points) == 0


def part1(sea_floor_map: dict) -> int:
    low_points = []

    for k, v in sea_floor_map.items():
        if is_low_point(sea_floor_map, k):
            low_points.append(v)

    return sum([x + 1 for x in low_points])


def get_data(path) -> dict:
    data = {}

    with open(path) as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    for i, row in enumerate(lines):
        for j, val in enumerate(row):
            data[(j, i)] = int(val)

    return data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)

    print(data)
    print(f'part 1: {part1(get_data(file_name))}')
    # print(f'part 2: {part2(get_data(file_name))}')
