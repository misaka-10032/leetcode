# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        best = 0
        prev = [0] * n
        for i in xrange(m):
            curr = [0] * n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    c1 = prev[j-1] if j > 0 else 0
                    c2 = prev[j]
                    c3 = curr[j-1] if j > 0 else 0
                    l = 1 + min(c1, c2, c3)
                    best = max(best, l*l)
                    curr[j] = l
            prev = curr
        return best
