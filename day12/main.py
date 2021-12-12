#! /usr/bin/env python3
import sys


class Cave:
    def __init__(self, name: str):
        self.name = name.upper() if name in ['start', 'end'] else name
        self.links = {}

    def __str__(self):
        # return f'{self.name} -> {[o.name for o in self.links]} '
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def remove(self, other: 'Cave'):
        del self.links[other]

    def add(self, other: 'Cave'):
        self.links[other] = other

    def contains(self, other: 'Cave'):
        return other in self.links

    def dead_end(self, came_from: 'Cave') -> bool:
        return len(self.links) == 0 or (len(self.links) == 1 and came_from in self.links)

    def is_start(self) -> bool:
        return self.name == 'START'

    def is_end(self) -> bool:
        return self.name == 'END'

    def is_small(self) -> bool:
        return self.name.islower()


def get_data(path) -> [list[list[str]]]:
    with open(path) as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    return [x.split('-') for x in lines]


def part1(lst: list[list[str]]) -> int:
    caves = {}

    for a, b in lst:
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

    return len(walk(caves['start'], [caves['start']]))


def walk(start_at: Cave, path: list[Cave]) -> list[list[Cave]]:
    if start_at.is_end():
        return [path]

    paths = []

    for cave in start_at.links:
        if cave.is_start():
            continue

        if cave.is_small() and cave in path:
            continue

        tmp_path = list([x for x in path])
        tmp_path.append(cave)

        paths += walk(cave, tmp_path)

    return paths


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
