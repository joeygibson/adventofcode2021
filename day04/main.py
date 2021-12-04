#! /usr/bin/env python3
import sys


def mark(board: list, ball: str):
    for row in board:
        for cell in row:
            if ball in cell:
                cell[ball] = True


def compute(board: list) -> int:
    res = 0
    print(f'board: {board}')
    for row in board:
        for cell in row:
            if not list(cell.values())[0]:
                print(f'cell: {int(list(cell)[0])}')
                res += int(list(cell)[0])

    return res


def part1(boards: list, balls: list) -> int:
    for ball in balls:
        for board in boards:
            mark(board, ball)

            if is_winner(board):
                res = compute(board)
                return res * int(ball)


def get_data(path):
    with open(path) as f:
        return [x.strip() for x in f.readlines() if x.strip()]


def create_boards(lst: list) -> list:
    boards = []

    while len(lst) >= 5:
        rows = list(map(lambda x: x.split(), lst[0:5]))
        rows = list(map(lambda x: [{x[i]: False} for i in range(0, len(x))], rows))
        boards.append(rows)

        lst = lst[5:]

    return boards


def is_winner(board: list) -> bool:
    for row in board:
        if all(list(map(lambda x: list(x.values())[0], row))):
            return True

    for i in range(0, len(board[0])):
        col = list(map(lambda x: x[i], board))
        if all(list(list(map(lambda x: list(x.values())[0], col)))):
            return True

    return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: main.py <filename>')
        sys.exit(1)

    lines = get_data(sys.argv[1])
    # lines = get_data('input0.txt')

    balls = lines[0].split(',')
    boards = create_boards(lines[1:])

    r1 = part1(boards, balls)
    # r2 = part2(lines)

    print(f'part 1: {r1}')
    # print(f'part 2: {r2}')
