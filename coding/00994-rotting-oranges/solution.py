#!/usr/bin/env python3
# encoding: utf-8

import collections
import dataclasses
from typing import List, Tuple


@dataclasses.dataclass
class RottenOrange:
    loc: Tuple[int, int]
    ts: int


class Solution:
    def move(self, loc: Tuple[int, int], delta: Tuple[int, int]):
        return loc[0] + delta[0], loc[1] + delta[1]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not n:
            return 0
        m = len(grid[0])
        if not m:
            return 0
        state = [[0 for _ in range(m)] for _ in range(n)]
        seeds = collections.deque()
        for y in range(n):
            for x in range(m):
                v = state[y][x] = grid[y][x]
                if v == 2:
                    seeds.append(RottenOrange(loc=(x, y), ts=0))

        max_ts = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while seeds:
            seed = seeds.popleft()
            for d in dirs:
                x, y = self.move(seed.loc, d)
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if state[y][x] == 1:
                    ts = seed.ts + 1
                    max_ts = max(max_ts, ts)
                    state[y][x] = 2
                    seeds.append(RottenOrange(loc=(x, y), ts=ts))
        for y in range(n):
            for x in range(m):
                if state[y][x] == 1:
                    return -1
        return max_ts
