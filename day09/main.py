#! /usr/bin/env python3
import functools
import itertools
import sys
from typing import Tuple


def is_low_point(sea_floor_map: dict, point: Tuple[int, int]) -> bool:
    point_depth = sea_floor_map[point]
    x, y = point

    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    depths = [sea_floor_map.get(n) for n in neighbors]
    valid_depths = list(filter(lambda d: d is not None, depths))
    low_points = list(filter(lambda d: d <= point_depth, valid_depths))

    return len(low_points) == 0


def part1(sea_floor_map: dict) -> int:
    low_points = []

    for k, v in sea_floor_map.items():
        if is_low_point(sea_floor_map, k):
            low_points.append(v)

    return sum([x + 1 for x in low_points])


# , width: int, height: int
def get_neighbors(point: Tuple) -> list[Tuple]:
    x, y = point
    # return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
    # return list(filter(lambda p: 0 <= p[0] <= width and 0 <= p[1] <= height, tmp))


def filter_not_nines(sea_floor_map: dict, points: list[Tuple]) -> list[Tuple]:
    return list(set([p for p in points if sea_floor_map.get(p) is not None and sea_floor_map.get(p) != 9]))


# def part2(sea_floor_map: dict) -> int:
#     basins = []
#     max_pos = max(sea_floor_map.keys())
#
#     for point in [x[0] for x in sea_floor_map.items() if x[1] != 9]:
#         neighbors = filter_not_nines(sea_floor_map, get_neighbors(point, *max_pos))
#         added = False
#
#         for basin in basins:
#             if any([x in basin for x in neighbors]):
#                 added = True
#                 basin.append(point)
#                 break
#
#         if not added:
#             n2 = filter_not_nines(sea_floor_map,
#                                   list(itertools.chain(*[get_neighbors(n, *max_pos) for n in neighbors])))
#
#             for basin in basins:
#                 if any([x in basin for x in n2]):
#                     added = True
#                     basin.append(point)
#                     break
#
#             if not added:
#                 basins.append([point])
#
#     for basin in basins:
#         print(basin)
#
#     print(f'basins count {len(basins)}')
#
#     sizes = list(reversed(sorted([len(basin) for basin in basins])))
#     print(f'sizes: {sizes}')
#     print(f'picks: {sizes[0:3]}')
#     return functools.reduce(lambda acc, n: acc * n, sizes[0:3], 1)

def part2(sea_floor_map: dict) -> int:
    big_basins = [0, 0, 0]

    for key in list(sea_floor_map.keys()):
        point = sea_floor_map.get(key)
        tmp = explore(sea_floor_map, point)
        basin = len(set(tmp))

        if big_basins[0] < basin:
            big_basins = big_basins[1:3]
            big_basins.append(basin)
            big_basins = sorted(big_basins)
        print(f'big_basins {big_basins}')

    return functools.reduce(lambda acc, n: acc * n, big_basins, 1)


def explore(filtered_map, point, basin=[]) -> list:
    if point is None:
        return basin

    del filtered_map[point]
    basin.append(point)

    res = [explore(filtered_map, filtered_map.get(n), basin) for n in get_neighbors(point)]
    return list(itertools.chain(*res))


def get_data(path) -> dict:
    data = {}

    with open(path) as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    for i, row in enumerate(lines):
        for j, val in enumerate(row):
            if val != '9':
                data[(j, i)] = (j, i)
            # data[(j, i)] = int(val)

    return data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)

    print(data)
    # print(f'part 1: {part1(get_data(file_name))}')
    print(f'part 2: {part2(get_data(file_name))}')
