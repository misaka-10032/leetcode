# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[1] * n for _ in xrange(m)]
        for k in xrange(m+1):
            if k >= m or obstacleGrid[k][0] == 1:
                break
        for i in xrange(k, m):
            f[i][0] = 0

        for k in xrange(n+1):
            if k >= n or obstacleGrid[0][k] == 1:
                break
        for j in xrange(k, n):
            f[0][j] = 0

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
