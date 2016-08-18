# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def flood(self, i, j):
        Q = deque()
        Q.append((i, j))
        self.grid[i][j] = 'F'
        while Q:
            i, j = Q.popleft()
            for di, dj in self.dirs:
                ii, jj = i+di, j+dj
                if ii < 0 or ii >= self.m:
                    continue
                if jj < 0 or jj >= self.n:
                    continue
                if self.grid[ii][jj] != '1':
                    continue
                self.grid[ii][jj] = 'F'
                Q.append((ii, jj))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        if self.m == 0 or self.n == 0:
            return 0

        cnt = 0
        for i in xrange(self.m):
            for j in xrange(self.n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.flood(i, j)

        for i in xrange(self.m):
            for j in xrange(self.n):
                if grid[i][j] == 'F':
                    grid[i][j] = '1'

        return cnt
