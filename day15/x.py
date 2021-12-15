#!/usr/bin/env python3

# "borrowed" from https://topaz.github.io/paste/#XQAAAQAIBwAAAAAAAAA0m0pnuFI8c/fBNAn6x25rtjB4jtldKRL87i//mqAHVHSbTT7z0TG5tgM7yMqCN/z2UtIUEhLFdHNHQSoP4tFmXkflYNQ6xKd2m+BFwAzA5wDCEnTpvsAA8O0Qj9h1WFI6kFSkVbBj2Z7IGmkJPr3wUUHP+mUNQAwqLwQrfuwLC46kPFEGKoOSu+4ijcc75b8AiMi1O7J8Zzhk0xwtUY4feiMOmfXSrL6ysDTK+aI3uFp/RX8xn06E7pG4aeIlR5wecoRqOOsXe5bCLAwSERfQ4tIlgEROGlNcyk0pZrW5RHdRceXqV78M3Ld2uuLvb3MFgv9TPB5dsRwatVWjVrF7KgDZGf5Na2wSHW8jx5RX0YT9SVFUusRYph0DZtQp0lgmMMxD5W4TpBtrMH4U810qlXaGpexlCOCg0aUnho1IIZETPjPGr+c7w7kZjeQP/YwECQ17wTP6lH3niXLmMipsSjvn13SCnz6MujWW31zqxuTlOC9RnZO8FeFAmkBSz+EGNqxoM2aC/51RgkKTV3cRQMHzoc4RA9b56YbmahWDb8V93UNRqzZqJkY6JMoCSHLJcKgqazd+CrWmmwvCjkxIVTB08kllLzni9qyWOSYT8q0tUH7OaNat5hqUxK8O3YgHAP4xy3Lo6WoRJJF6xq1fHZXX/zdu0huMac08ZcbocBijrJYcPXQDPWoIgc5oyJFzshCwjpA/nl9i6aXcI07VwhAmy7PjqiR0xA6IxB+lSyQ48G88k2su0BRJZN0//EuUKP6ZBejNpoogFrrreTypUkK+kaY2UEnkAiTol/y3k2/Kak8qj5FfntVS9Q0lXq24swInHX8h9NS+HLVrey7bTnvaISLx+dnJ70HUe5l1HEkudO8y0IOzrtiU7bztzY8ePkeOjMBhexDE1E1Rb5sKmybUbPFWSdPreTWmBqDeI30hKUQ1lnd8jq5aHOEs2RFOSkYQYiR5zYcv54AVOzzHP3p6d5ZsHdFvtrcnxXYn5Wy/eIjRMBPyqP9PkWwA

import sys
from heapq import heappop, heappush
from itertools import product
from typing import Dict, List, Tuple

Pair = Tuple[int, int]
Graph = Dict[Pair, int]


def neighbours(v: Pair) -> List[Pair]:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return [(v[0] + dy, v[1] + dx) for dx, dy in directions]


def get_n_m(graph: Graph) -> Pair:
    n = max(y for y, _ in graph.keys()) + 1
    m = max(x for _, x in graph.keys()) + 1
    return n, m


def djikstra(graph: Graph, start: Pair, end: Pair) -> Dict[Pair, int]:
    dist: Dict[Pair, int] = {start: 0}
    pq: List[Tuple[int, Pair]] = []

    for v in graph.keys():
        if v != start:
            dist[v] = int(1e9)
        heappush(pq, (dist[v], v))

    while pq:
        _, u = heappop(pq)
        if u == end:
            return dist
        for v in neighbours(u):
            if v not in graph:
                continue
            alt = dist[u] + graph[v]
            if alt < dist[v]:
                dist[v] = alt
                heappush(pq, (alt, v))
    return dist


def read_problem() -> Graph:
    return {
        (i, j): int(val)
        for i, line in enumerate(sys.stdin)
        for j, val in enumerate(line.strip())
    }


def replicate_map(graph: Graph) -> Graph:
    graph = graph.copy()
    n, m = get_n_m(graph)
    for ix, jx, i, j in product(range(5), range(5), range(n), range(m)):
        graph[ix * n + i, jx * m + j] = (ix + jx + graph[i, j] - 1) % 9 + 1

    return graph


def solve(problem: Graph) -> int:
    n, m = get_n_m(problem)
    start, end = (0, 0), (n - 1, m - 1)
    dist = djikstra(problem, start, (n - 1, m - 1))
    return dist[end]


if __name__ == "__main__":
    problem = read_problem()
    print("Part 1:", solve(problem))
    print("Part 2:", solve(replicate_map(problem)))

