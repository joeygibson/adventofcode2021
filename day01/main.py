# /usr/bin/env python3

# Press the green button in the gutter to run the script.
import sys


def part1(path: str) -> None:
    with open(path) as f:
        lines = [int(x) for x in f.readlines()]

    res = [ind + 1 for ind, x in enumerate(lines) if ind + 1 < len(lines) and lines[ind + 1] > x]
    print(res)
    print(len(res))


if __name__ == '__main__':
    part1(sys.argv[1])
