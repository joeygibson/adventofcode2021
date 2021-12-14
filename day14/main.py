#! /usr/bin/env python3
import itertools
import sys
from collections import Counter, defaultdict
from typing import Tuple


def get_data(path) -> (list[str], dict[str, str]):
    with open(path) as f:
        lines = f.readlines()

    template = [c for c in lines[0].strip()]

    rules = {}
    for line in itertools.dropwhile(lambda x: '->' not in x, lines):
        splits = line.strip().split(' -> ')
        rules[splits[0].strip()] = splits[1].strip()

    return template, rules


def partition(lst: list, n: int) -> Tuple:
    for i in range(0, len(lst) - 1):
        a = lst[i]
        b = lst[i + 1]
        yield a, b


def combine(template: list[str], rules: dict[str, str], iterations: int = 10) -> int:
    pairs = Counter()

    for pair in partition(template, 1):
        pairs[pair] = 1

    for i in range(iterations):
        print(f'iteration {i + 1}')
        next_pairs = Counter()

        for (a, b), tally in pairs.items():
            i = rules[''.join([a, b])]
            next_pairs[(a, i)] += tally
            next_pairs[(i, b)] += tally

        pairs = next_pairs

    totals = defaultdict(lambda: 0)

    for (a, b), tally in pairs.items():
        totals[a] += tally

    totals[template[-1]] += 1

    min_val = min(totals.values())
    max_val = max(totals.values())

    return max_val - min_val


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
