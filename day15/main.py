#! /usr/bin/env python3
import sys
from typing import Tuple

Pair = Tuple[int, int]


class Spot:
    def __init__(self, position: Pair, parent: 'Spot' = None, risk: int = 0):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
        self.risk = risk

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.risk < other.risk

    def __repr__(self):
        return f'({self.position}, {self.f} ({self.risk}))'


def get_data(path) -> dict[Pair, int]:
    with open(path) as f:
        lines = f.readlines()

    the_map = {}

    for j, row in enumerate(lines):
        for i, val in enumerate(row.strip()):
            the_map[(i, j)] = int(val)

    return the_map


def part1(the_map: dict[Pair, int]) -> [Pair]:
    start_pos = min(the_map.keys())
    goal_pos = max(the_map.keys())

    start = Spot(start_pos, risk=the_map[start_pos])
    goal = Spot(goal_pos, risk=the_map[goal_pos])

    open = []
    closed = []

    open.append(start)

    while len(open) > 0:
        open.sort()

        current = open.pop(0)

        closed.append(current)

        if current == goal:
            path = []
            while current != start:
                path.append(current.position)
                current = current.parent

            for spot in reversed(path):
                print(f'{spot} => {the_map[spot]}')

            res = sum([the_map[spot] for spot in path])

            return res

        x, y = current.position

        neighbors = [(x + 1, y), (x, y + 1)]

        for next in neighbors:
            map_value = the_map.get(next)

            if map_value is None:
                continue

            neighbor = Spot(next, current, risk=map_value)

            if neighbor is closed:
                continue

            neighbor.g = abs(neighbor.position[0] - start.position[0]) + \
                         abs(neighbor.position[1] - start.position[1])
            neighbor.h = abs(neighbor.position[0] - goal.position[0]) + \
                         abs(neighbor.position[1] - goal.position[1])
            neighbor.f = neighbor.g + neighbor.h + neighbor.risk

            if add_to_open(open, neighbor):
                open.append(neighbor)

    return None


def add_to_open(open: list[Spot], neighbor: Spot) -> bool:
    for node in open:
        print(f'{neighbor.f} <=> {node.f}')
        if neighbor == node and neighbor.f >= node.f:
            return False

    return True


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
