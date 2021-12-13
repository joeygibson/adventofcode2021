#! /usr/bin/env python3
import itertools
import sys


def get_data(path) -> (list[list[str]], list[str]):
    with open(path) as f:
        lines = [x.strip() for x in f.readlines()]

    position_lines = list(itertools.takewhile(lambda x: ',' in x, lines))
    instruction_lines = list(itertools.dropwhile(lambda x: '=' not in x, lines))

    positions = [x.split(',') for x in position_lines]
    max_x = max([int(x[0]) for x in positions])
    max_y = max([int(x[1]) for x in positions])

    print(f'max: {max_x}, {max_y}')

    map_dict = {}

    for x, y in positions:
        point = (int(x), int(y))
        map_dict[point] = '#'

    the_map = []

    for y in range(max_y + 1):
        row = [map_dict.get((x, y), '.') for x in range(max_x + 1)]
        the_map.append(row)

    instructions = [i[11:].split('=') for i in instruction_lines]
    instructions = list(map(lambda x: [x[0], int(x[1])], instructions))

    return the_map, instructions


def part1(the_map: list[list[str]], instructions) -> int:
    for axis, fold_line in instructions:
        if axis == 'y':
            end = len(the_map) - 1

            for line_no in range(end, fold_line, -1):
                matching_line_no = fold_line - (line_no - fold_line)
                line = the_map[line_no]
                mline = the_map[matching_line_no]

                merged_line = ['#' if a == '#' or b == '#' else '.' for a, b in zip(line, mline)]
                the_map[matching_line_no] = merged_line
                del the_map[line_no]
        else:
            end = len(the_map[0]) - 1

            for col_no in range(end, fold_line, -1):
                matching_col_no = fold_line - (col_no - fold_line)

                col = list(map(lambda x: x[col_no], the_map))
                mcol = list(map(lambda x: x[matching_col_no], the_map))

                for line_no, line in enumerate(the_map):
                    val = '#' if col[line_no] == '#' or mcol[line_no] == '#' else '.'
                    line[matching_col_no] = val
                    del line[col_no]

    for row in the_map:
        print(''.join(['#' if x == '#' else ' ' for x in row]))

    return len(list(filter(lambda x: x == '#', itertools.chain(*the_map))))


def part2(the_map: list[list[str]], instructions) -> int:
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(*get_data(file_name))}')
    # print(f'part2 {part2(get_data(file_name))}')
