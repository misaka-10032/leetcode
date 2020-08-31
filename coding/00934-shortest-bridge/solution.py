#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List, Set, Tuple


class Solution:
    def _touches(self, i: int, j: int, dst: Set[int]) -> bool:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i2, j2 = i + di, j + dj
            if (i2, j2) in dst:
                return True
        return False

    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 1
        m, n = len(A), len(A[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def _visit(i: int, j: int, island: Set[Tuple[int, int]]):
            visited[i][j] = True
            island.add((i, j))
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i + di, j + dj
                if (0 <= i2 < m and 0 <= j2 < n and A[i2][j2] == 1 and
                        not visited[i2][j2]):
                    _visit(i2, j2, island)

        islands = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not visited[i][j]:
                    island = set()
                    _visit(i, j, island)
                    islands.append(island)
        if len(islands) != 2:
            return 1
        src, dst = islands
        if len(dst) < len(src):
            src, dst = dst, src

        queue = collections.deque()
        for i, j in src:
            queue.append((i, j, 0))
        while queue:
            i, j, d = queue.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and A[i2][j2] == 0:
                    if self._touches(i2, j2, dst):
                        return d + 1
                    A[i2][j2] = 1
                    queue.append((i2, j2, d + 1))
        return 1
