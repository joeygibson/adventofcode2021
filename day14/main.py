#! /usr/bin/env python3
import itertools
import sys
from collections import Counter


def get_data(path) -> (list[str], dict[str, str]):
    with open(path) as f:
        lines = f.readlines()

    template = [c for c in lines[0].strip()]

    # rules = {splits[0].strip(): splits[1].strip()
    #          for line in itertools.dropwhile(lambda x: '->' not in x, lines)
    #          for splits in line.split(' -> ')}
    rules = {}
    for line in itertools.dropwhile(lambda x: '->' not in x, lines):
        splits = line.strip().split(' -> ')
        rules[splits[0].strip()] = splits[1].strip()

    return template, rules


def partition(lst: list, n: int) -> list:
    for i in range(0, len(lst) - 1):
        yield lst[i:i + 2]


def combine(template: list[str], rules: dict[str, str], iterations: int = 10) -> int:
    current = template

    for i in range(iterations):
        print(f'iteration {i + 1}')
        new = []

        pairs = list(partition(current, 1))
        new_vals = [rules[''.join(pair)] for pair in pairs]
        for index, c in enumerate(current):
            if index >= len(new_vals):
                new += [c]
            else:
                new += [c, new_vals[index]]

        current = new

    counts = Counter(current)

    max_elem = max(counts.values())
    min_elem = min(counts.values())

    return max_elem - min_elem


def part1(template: list[str], rules: dict[str, str]) -> int:
    return combine(template, rules)


def part2(template: list[str], rules: dict[str, str]) -> int:
    return combine(template, rules, 40)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(*get_data(file_name))}')
    print()
    print(f'part2 {part2(*get_data(file_name))}')
