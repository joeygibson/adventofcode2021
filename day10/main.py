#! /usr/bin/env python3
import functools
import sys

OPENERS = '([{<'
CLOSERS = ')]}>'
PAIRS = {c: o for c, o in zip(CLOSERS, OPENERS)}
PART1_SCORE_VALUES = {ch: s for ch, s in zip(CLOSERS, [3, 57, 1197, 25137])}
PART2_SCORE_VALUES = {ch: s for ch, s in zip(OPENERS, range(1, 5))}


def part1(rows: list[list[str]]) -> (int, list[str]):
    offenders = {}
    offending_rows = []

    for row in rows:
        stack = []
        for ch in row:
            if ch in PAIRS.keys():
                if len(stack) == 0:
                    offenders[ch] = 1
                    offending_rows.append(row)
                    break
                else:
                    top = stack[-1]
                    opener = PAIRS[ch]
                    if top != opener:
                        offenders[ch] = offenders.get(ch, 0) + 1
                        offending_rows.append(row)
                        break
                    else:
                        stack.pop()
            else:
                stack.append(ch)

    total = functools.reduce(lambda acc, ch: acc + (offenders.get(ch, 0) *
                                                    PART1_SCORE_VALUES[ch]),
                             PAIRS.keys(), 0)

    return total, offending_rows


def part2(rows: list[list[str]]) -> int:
    scores = []

    for row in rows:
        stack = []
        for ch in row:
            if ch in PAIRS.keys():
                stack.pop()
            else:
                stack.append(ch)

        scores.append(functools.reduce(lambda acc, ch: (acc * 5) + PART2_SCORE_VALUES[ch], reversed(stack), 0))

    sorted_scores = sorted(scores)

    return sorted_scores[int(len(sorted_scores) / 2)]


def get_data(path) -> list[list[str]]:
    with open(path) as f:
        return [list(x.strip()) for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)

    p1, offending_rows = part1(get_data(file_name))

    print(f'part 1: {p1}')

    good_data = [row for row in data if row not in offending_rows]

    print(f'part 2: {part2(good_data)}')
