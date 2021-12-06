#! /usr/bin/env python3
import sys


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


def get_data(path) -> list:
    with open(path) as f:
        return [Lanternfish(x) for x in map(int, f.read().strip().split(','))]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: main.py <filename> <iterations>')
        sys.exit(1)

    fish = get_data(sys.argv[1])
    r1 = part1(fish, int(sys.argv[2]))

    print(f'part 1: {r1}')
    # print(f'part 2: {r2}')
