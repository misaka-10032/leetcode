# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* for each building, accumulate its distance to all
  possible lands
* find the land with min dist
* special care for unreachable
  * if some land is unreachable to any of the building,
    it can be taken as obstacle. rationale is that if
    it's unreachable, it can also not be used as intermediate
    path by other buildings (proof by contradictory).
"""

from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs_acc(i, j):
            Q = deque([(i, j, 0)])
            visited = [[False] * n for _ in xrange(m)]
            visited[i][j] = True
            while Q:
                i, j, d = Q.popleft()
                for di, dj in dirs:
                    ii = i + di
                    jj = j + dj
                    if ii < 0 or ii >= m or \
                       jj < 0 or jj >= n or \
                       visited[ii][jj] or grid[ii][jj] != 0:
                        continue
                    visited[ii][jj] = True
                    dist[ii][jj] += d + 1
                    Q.append((ii, jj, d+1))

            for i in xrange(m):
                for j in xrange(n):
                    if not visited[i][j] and grid[i][j] == 0:
                        grid[i][j] = 2

        if not grid or not grid[0]:
            return -1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        dist = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    bfs_acc(i, j)

        inf = 999999999
        smallest = inf
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    smallest = min(smallest, dist[i][j])
        return smallest if smallest != inf else -1
