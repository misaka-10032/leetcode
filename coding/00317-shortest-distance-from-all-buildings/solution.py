#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])

        dists = [[0 for _ in range(n)] for _ in range(m)]

        def _bfs(i0: int, j0: int):
            visited = [[False for _ in range(n)] for _ in range(m)]
            queue = collections.deque([(i0, j0, 0)])
            while queue:
                i1, j1, d = queue.popleft()
                d += 1
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    i2, j2 = i1 + di, j1 + dj
                    if (0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0 and
                            not visited[i2][j2]):
                        visited[i2][j2] = True
                        dists[i2][j2] += d
                        queue.append((i2, j2, d))
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and not visited[i][j]:
                        # Such empty land is unreachable. Treat it as obstacle
                        grid[i][j] = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    _bfs(i, j)

        shortest = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if shortest > 0:
                    shortest = min(shortest, dists[i][j])
                else:
                    shortest = dists[i][j]
        return shortest
