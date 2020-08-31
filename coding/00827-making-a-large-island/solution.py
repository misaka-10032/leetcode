#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # First, find the connected components
        pos_to_island_idx_map = {}
        island_sizes = []

        def _visit(i: int, j: int, island_idx: int):
            pos_to_island_idx_map[(i, j)] = island_idx
            island_sizes[island_idx] += 1
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i + di, j + dj
                if (0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] and
                        (i2, j2) not in pos_to_island_idx_map):
                    _visit(i2, j2, island_idx)

        island_cnt = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                if (i, j) in pos_to_island_idx_map:
                    continue
                island_sizes.append(0)
                _visit(i, j, island_cnt)
                island_cnt += 1

        if not island_cnt:
            return 1

        # Then, iterate the possible 0's, and see if we can make a larger area.
        max_size = max(island_sizes)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    continue
                adj_island_ids = set()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2]:
                        adj_island_ids.add(pos_to_island_idx_map[(i2, j2)])
                size = 1
                for island_idx in adj_island_ids:
                    size += island_sizes[island_idx]
                max_size = max(max_size, size)
        return max_size
