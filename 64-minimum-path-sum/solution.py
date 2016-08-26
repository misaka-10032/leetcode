# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        f = [[0] * n for _ in xrange(m)]
        f[0][0] = grid[0][0]
        for i in xrange(1, m):
            f[i][0] = grid[i][0] + f[i-1][0]
        for j in xrange(1, n):
            f[0][j] = grid[0][j] + f[0][j-1]

        for i in xrange(1, m):
            for j in xrange(1, n):
                f[i][j] = grid[i][j] + min(f[i-1][j], f[i][j-1])

        return f[m-1][n-1]
