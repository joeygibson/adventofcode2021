#! /usr/bin/env python3
import sys
from collections import Counter


class Lanternfish:
    def __init__(self, age: int = 0):
        self._age = age

    def __str__(self):
        return f'Lanternfish(age: {self._age})'

    def age(self):
        if self._age == 0:
            self._age = 6
        else:
            self._age -= 1

    def is_read_to_spawn(self) -> bool:
        return self._age == 0


def part1(fish: list[Lanternfish], iterations: int) -> int:
    for i in range(0, iterations):
        new_fish = []

        for f in fish:
            if f.is_read_to_spawn():
                new_fish.append(Lanternfish(8))

            f.age()

        fish += new_fish

    return len(fish)


def part2(fish: list[int], iterations: int) -> int:
    fish_counts = Counter(fish)

    for i in range(0, iterations):
        for k, v in sorted(fish_counts.items(), key=lambda pair: pair[0]):
            print(f'{k}: {v}', end=', ')

        births = fish_counts.get(0) if fish_counts.get(0) is not None else 0
        print(f' births {births}')
        for day in range(1, 9):
            fish_counts[day - 1] = fish_counts.get(day) if fish_counts.get(day) is not None else 0

        fish_counts[8] = births
        fish_counts[6] = fish_counts.get(6) + births

    return sum(fish_counts.values())


def get_as_fish(path) -> list:
    with open(path) as f:
        return [Lanternfish(x) for x in map(int, f.read().strip().split(','))]


def get_as_ints(path) -> list:
    with open(path) as f:
        return [int(x) for x in f.read().strip().split(',')]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: main.py <filename> <iterations>')
        sys.exit(1)

    file_name = sys.argv[1]
    iterations = int(sys.argv[2])

    # r1 = part1(get_as_fish(file_name), iterations)
    r2 = part2(get_as_ints(file_name), iterations)

    # print(f'part 1: {r1}')
    print(f'part 2: {r2}')
