#! /usr/bin/env python3
import sys
from collections import Counter


class Cave:
    def __init__(self, name: str):
        self.name = name.upper() if name in ['start', 'end'] else name
        self.links = {}

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def add(self, other: 'Cave'):
        self.links[other] = other

    def is_start(self) -> bool:
        return self.name == 'START'

    def is_end(self) -> bool:
        return self.name == 'END'

    def is_small(self) -> bool:
        return self.name.islower()


def get_data(path) -> [list[list[str]]]:
    with open(path) as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    caves = {}

    for a, b in [x.split('-') for x in lines]:
        if a not in caves:
            a_cave = Cave(a)
        else:
            a_cave = caves[a]

        if b not in caves:
            b_cave = Cave(b)
        else:
            b_cave = caves[b]

        a_cave.add(b_cave)
        b_cave.add(a_cave)

        caves[a] = a_cave
        caves[b] = b_cave

    return caves


def part1(caves: dict[str, Cave]) -> int:
    return len(walk(caves['start'], [caves['start']], False))


def part2(caves: dict[str, Cave]) -> int:
    return len(walk(caves['start'], [caves['start']], True))


def walk(start_at: Cave, path: list[Cave], allow_multiple: bool) -> list[list[Cave]]:
    if start_at.is_end():
        return [path]

    paths = []

    for cave in start_at.links:
        if cave.is_start():
            continue

        if cave.is_small() and cave in path:
            if allow_multiple:
                small_counts = Counter(list(filter(lambda x: x.is_small(), path)))
                multiple_small_visits = any([c > 1 for c in small_counts.values()])

                if multiple_small_visits:
                    continue
            else:
                continue

        tmp_path = list([x for x in path])
        tmp_path.append(cave)

        paths += walk(cave, tmp_path, allow_multiple)

    return paths


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print(f'part2 {part2(get_data(file_name))}')
