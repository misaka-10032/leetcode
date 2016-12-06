# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Memorized dfs
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if cache[i][j] > 0:
                return cache[i][j]

            _best = 0
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if ii < 0 or ii >= m or \
                   jj < 0 or jj >= n or \
                   matrix[ii][jj] <= matrix[i][j]:
                    continue
                _best = max(_best, dfs(ii, jj))
            cache[i][j] = _best + 1
            return cache[i][j]

        if not matrix or not matrix[0]:
            return 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m = len(matrix)
        n = len(matrix[0])
        cache = [[0] * n for _ in xrange(m)]

        best = 0
        for i in xrange(m):
            for j in xrange(n):
                best = max(best, dfs(i, j))
        return best
