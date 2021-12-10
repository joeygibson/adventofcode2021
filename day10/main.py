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


def part1(rows: list[list[str]]) -> int:
    offenders = {}
    for row in rows:
        print(row)
        stack = []
        for ch in row:
            if ch in CLOSERS:
                if len(stack) == 0:
                    offenders[ch] = 1
                    break
                else:
                    top = stack[-1]
                    if (ch == R_PAREN and top != L_PAREN) or \
                            (ch == R_BRACKET and top != L_BRACKET) or \
                            (ch == R_CURLY and top != L_CURLY) or \
                            (ch == R_ANGLE and top != L_ANGLE):
                        offenders[ch] = offenders.get(ch, 0) + 1
                        break
                    else:
                        stack.pop()
            else:
                stack.append(ch)

    print(f'stack {stack}')
    print(f'offenders {offenders}')

    parens = offenders.get(R_PAREN, 0) * 3
    brackets = offenders.get(R_BRACKET, 0) * 57
    curlies = offenders.get(R_CURLY, 0) * 1197
    angles = offenders.get(R_ANGLE, 0) * 25137

    return sum([parens, brackets, curlies, angles])


def is_valid(row: list[str]) -> bool:
    chars = {'parens': 0, 'brackets': 0, 'curlies': 0, 'angles': 0}
    for ch in chars:
        if ch in [L_PAREN, R_PAREN]:
            chars['parens'] += 1
        elif ch in [L_BRACKET, R_BRACKET]:
            chars['brackets'] += 1
        elif ch in [L_CURLY, R_CURLY]:
            chars['curlies'] += 1
        else:
            chars['angles'] += 1

    return all([x % 2 == 0 for x in chars.values()])


def get_data(path) -> list[list[str]]:
    with open(path) as f:
        return [list(x.strip()) for x in f.readlines() if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]
    data = get_data(file_name)

    print(f'part 1: {part1(get_data(file_name))}')
    # print(f'part 2: {part2(get_data(file_name))}')
