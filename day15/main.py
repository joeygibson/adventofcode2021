#! /usr/bin/env python3
import sys
from collections import defaultdict
from copy import deepcopy
from typing import Tuple, Dict

Pair = Tuple[int, int]


class Graph:
    def __init__(self, the_map):
        self.nodes = set()
        self.distances = the_map

    def addNode(self, value):
        self.nodes.add(value)

    def edges(self, node):
        x, y = node
        neighbors = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        return [n for n in neighbors if self.distances.get(n) is not None]


def get_data(path) -> dict[Pair, int]:
    with open(path) as f:
        lines = f.readlines()

    the_map = {}

    for j, row in enumerate(lines):
        for i, val in enumerate(row.strip()):
            the_map[(i, j)] = int(val)

    return the_map


def get_exploded_data(path) -> Dict[Pair, int]:
    with open(path) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    cols = len(lines[0].strip())
    rows = len(lines)

    raw_map = [[0 for col in range(cols)] for row in range(rows)]

    for j, row in enumerate(lines):
        for i, val in enumerate(row.strip()):
            raw_map[j][i] = int(val)

    for row_num, row in enumerate(raw_map):
        new_row = deepcopy(row)
        current_vals = new_row
        for i in range(4):
            new_cols = [x + 1 if x + 1 <= 9 else 1 for x in current_vals]
            new_row += new_cols
            current_vals = new_cols

        raw_map[row_num] = new_row

    new_map = deepcopy(raw_map)
    current_map = deepcopy(new_map)
    for i in range(4):
        tmp_map = []
        for row in current_map:
            new_row = [x + 1 if x + 1 <= 9 else 1 for x in row]
            tmp_map.append(new_row)

        new_map += tmp_map
        current_map = tmp_map

    the_map = {}

    for j, row in enumerate(new_map):
        for i, val in enumerate(row):
            the_map[(i, j)] = val

    print('map created')
    return the_map


def dijkstra(graph, initial, goal):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges(minNode):
            weight = currentWeight + graph.distances[edge]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited[goal]


def part1(the_map: dict[Pair, int]) -> int:
    g = Graph(the_map)

    for node in the_map.keys():
        g.addNode(node)

    return dijkstra(g, min(the_map.keys()), max(the_map.keys()))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    # print(f'part1 {part1(get_data(file_name))}')
    print()
    print(f'part2 {part1(get_exploded_data(file_name))}')
