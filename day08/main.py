#! /usr/bin/env python3
import sys


def get_data(path) -> list:
    data = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            data.append([x.split() for x in line.split('|')])

    return data


def part1(lst: list[list[str]]) -> int:
    res = 0
    for _, displays in lst:
        for display in displays:
            segments = len(display)
            res += 1 if segments in [2, 3, 4, 7] else 0

    return res


def part2(lst: list[list[str]]) -> int:
    total = 0

    for patterns, displays in lst:
        matches = {}
        one = list(filter(lambda x: len(x) == 2, patterns))[0]
        four = list(filter(lambda x: len(x) == 4, patterns))[0]
        seven = list(filter(lambda x: len(x) == 3, patterns))[0]
        eight = list(filter(lambda x: len(x) == 7, patterns))[0]
        fourdiff = four.replace(one[0], '').replace(one[1], '')

        matches[''.join(sorted(one))] = '1'
        matches[''.join(sorted(four))] = '4'
        matches[''.join(sorted(seven))] = '7'
        matches[''.join(sorted(eight))] = '8'

        for p in patterns:
            sorted_p = ''.join(sorted(p))
            if p == one or p == four or p == seven or p == eight:
                continue
            if len(p) == 5:
                if set(one).issubset(p):
                    matches[sorted_p] = '3'
                elif set(fourdiff).issubset(p):
                    matches[sorted_p] = '5'
                else:
                    matches[sorted_p] = '2'
            elif len(p) == 6:
                if set(four).issubset(p):
                    matches[sorted_p] = '9'
                elif set(fourdiff).issubset(p):
                    matches[sorted_p] = '6'
                else:
                    matches[sorted_p] = '0'

        if len(matches) == 10:
            vals = [matches[''.join(sorted(x))] for x in displays]
            val = int(''.join(vals))
            total += val

    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)

    print(f'part 1: {part1(get_data(file_name))}')
    print(f'part 2: {part2(get_data(file_name))}')
