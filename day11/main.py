#! /usr/bin/env python3
import itertools
import sys
from typing import Tuple


class Octopus:
    def __init__(self, x: int, y: int, power: int):
        self.x = x
        self.y = y
        self.power = power
        self.flashed = False

    def __str__(self) -> str:
        return f'Octopus(({self.x}, {self.y}): {self.power}, {self.flashed}'

    def neighbors(self) -> list[Tuple[int, int]]:
        return [(self.x, self.y - 1),  # up
                (self.x - 1, self.y),  # left
                (self.x, self.y + 1),  # down
                (self.x + 1, self.y),  # right
                (self.x - 1, self.y - 1),  # up-left
                (self.x + 1, self.y - 1),  # up-right
                (self.x - 1, self.y + 1),  # down-left
                (self.x + 1, self.y + 1)]  # down-right

    def increase_power(self) -> bool:
        self.power += 1

        if self.power == 10:
            self.flashed = True
            self.power = 0

        return self.flashed

    def can_increase(self) -> bool:
        return not self.flashed

    def reset(self):
        self.flashed = False


def get_data(path) -> dict[Tuple[int, int], Octopus]:
    data = {}

    with open(path) as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    for i, row in enumerate(lines):
        for j, val in enumerate(row):
            data[(j, i)] = Octopus(j, i, int(val))

    return data


def part1(octopuses: dict[Tuple[int, int], Octopus], iterations: int) -> int:
    def step(candidates: list[Octopus]) -> int:
        neighbors = []
        flashed = 0
        for octopus in candidates:
            if octopus.can_increase() and octopus.increase_power():
                flashed += 1
                neighbors.append(octopus.neighbors())

        neighbors = list(itertools.chain(*neighbors))
        valid_neighbors = [octopuses[n] for n in neighbors if n in octopuses and not octopuses[n].flashed]

        if len(valid_neighbors) > 0:
            return flashed + step(valid_neighbors)
        else:
            return flashed

    total_flashes = 0

    for i in range(iterations):
        flashes = step(list(octopuses.values()))
        total_flashes += flashes
        for octopus in octopuses.values():
            octopus.reset()

    return total_flashes


def part2(octopuses: dict[Tuple[int, int], Octopus]) -> int:
    def step(candidates: list[Octopus]) -> int:
        neighbors = []
        flashed = 0
        for octopus in candidates:
            if octopus.can_increase() and octopus.increase_power():
                flashed += 1
                neighbors.append(octopus.neighbors())

        neighbors = list(itertools.chain(*neighbors))
        valid_neighbors = [octopuses[n] for n in neighbors if n in octopuses and not octopuses[n].flashed]

        if len(valid_neighbors) > 0:
            return flashed + step(valid_neighbors)
        else:
            return flashed

    all_flashed = -1

    for i in range(1000):
        flashes = step(list(octopuses.values()))
        # print(f'flashes: {flashes}, iter {i}')
        if flashes == 100:
            all_flashed = i + 1

            break

        for octopus in octopuses.values():
            octopus.reset()

        # print(f'{i} -> {flashes}')

    return all_flashed


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    iterations = int(sys.argv[2])

    print(f'part1 {part1(get_data(file_name), iterations)}')
    print(f'part2 {part2(get_data(file_name))}')
