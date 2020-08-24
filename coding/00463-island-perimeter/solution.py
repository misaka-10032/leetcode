#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def _is_water(i: int, j: int) -> bool:
            if 0 <= i < m and 0 <= j < n:
                return not grid[i][j]
            else:
                return True

        perimeter = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
                for di, dj in deltas:
                    i2, j2 = i + di, j + dj
                    if _is_water(i2, j2):
                        perimeter += 1
        return perimeter
