#! /usr/bin/env python3
import sys

L_PAREN = '('
R_PAREN = ')'
L_BRACKET = '['
R_BRACKET = ']'
L_CURLY = '{'
R_CURLY = '}'
L_ANGLE = '<'
R_ANGLE = '>'

OPENERS = [L_PAREN, L_BRACKET, L_CURLY, L_ANGLE]
CLOSERS = [R_PAREN, R_BRACKET, R_CURLY, R_ANGLE]


def part1(rows: list[list[str]]) -> (int, list[str]):
    offenders = {}
    offending_rows = []
    for row in rows:
        stack = []
        for ch in row:
            if ch in CLOSERS:
                if len(stack) == 0:
                    offenders[ch] = 1
                    offending_rows.append(row)
                    break
                else:
                    top = stack[-1]
                    if (ch == R_PAREN and top != L_PAREN) or \
                            (ch == R_BRACKET and top != L_BRACKET) or \
                            (ch == R_CURLY and top != L_CURLY) or \
                            (ch == R_ANGLE and top != L_ANGLE):
                        offenders[ch] = offenders.get(ch, 0) + 1
                        offending_rows.append(row)
                        break
                    else:
                        stack.pop()
            else:
                stack.append(ch)

    parens = offenders.get(R_PAREN, 0) * 3
    brackets = offenders.get(R_BRACKET, 0) * 57
    curlies = offenders.get(R_CURLY, 0) * 1197
    angles = offenders.get(R_ANGLE, 0) * 25137

    return sum([parens, brackets, curlies, angles]), offending_rows


def part2(rows: list[list[str]]) -> int:
    scores = []

    for row in rows:
        stack = []
        for ch in row:
            if ch in CLOSERS:
                stack.pop()
            else:
                stack.append(ch)

        score = 0

        for ch in reversed(stack):
            if ch == L_PAREN:
                ch_score = 1
            elif ch == L_BRACKET:
                ch_score = 2
            elif ch == L_CURLY:
                ch_score = 3
            else:
                ch_score = 4

            score = (score * 5) + ch_score

        scores.append(score)

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
