# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
        m = len(dungeon)
        n = len(dungeon[0])
        f = [[0] * n for _ in xrange(m)]
        f[m-1][n-1] = max(1, 1-dungeon[m-1][n-1])
        for i in xrange(m-2, -1, -1):
            f[i][n-1] = max(1, f[i+1][n-1]-dungeon[i][n-1])
        for j in xrange(n-2, -1, -1):
            f[m-1][j] = max(1, f[m-1][j+1]-dungeon[m-1][j])
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                f[i][j] = max(1, min(f[i+1][j], f[i][j+1])-dungeon[i][j])
        return f[0][0]
